from __future__ import absolute_import

from annoying.functions import get_object_or_None
from celery import shared_task
from io import BytesIO
from django.conf import settings
from os import makedirs
from os.path import join, normpath, exists
from rest_framework.parsers import JSONParser
from .playapi.googleplay import GooglePlayAPI
from .models import AppBuddyUser, AgentInfo, AppInfo


@shared_task
def download_app_from_playstore(*args, **kwargs):
    application_id = kwargs['app_id']
    app = get_object_or_None(AppInfo, pk=application_id)
    if app:
        app_name = "%s-%s.apk" % (app.package_name, app.app_version)
        apk_file = normpath(join(settings.APPLICATION_DOWNLOAD_ROOT, app_name))
        if not exists(settings.APPLICATION_DOWNLOAD_ROOT):
            makedirs(settings.APPLICATION_DOWNLOAD_ROOT)
        if not exists(apk_file):
            api = GooglePlayAPI(androidId=settings.ANDROID_DEVICE_ID)
            api.login(settings.GOOGLE_LOGIN_ID, settings.GOOGLE_PASSWORD)
            print app.app_version
            response = api.details(app.package_name)
            doc = response.docV2
            version = doc.details.appDetails.versionCode
            data = api.download(app.package_name, version)
            open(apk_file, "wb").write(data)


@shared_task
def log_appbuddy_install(*args, **kwargs):
    log_data = kwargs['log_data']
    stream = BytesIO(log_data)
    data = JSONParser().parse(stream)
    user = get_object_or_None(AppBuddyUser, device_id=data.get('device_id'))
    if user is None:
        agent_info = None
        agent = get_object_or_None(AgentInfo, agent_id=data.get('agent_id'))
        if len(agent) > 0:
            agent_info = agent[0]

        print agent
    pass


