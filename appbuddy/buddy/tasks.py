from __future__ import absolute_import

from annoying.functions import get_object_or_None
from celery import shared_task
from io import BytesIO
from django.conf import settings
from os import makedirs
from os.path import join, normpath, exists
from rest_framework.parsers import JSONParser
from .playapi.googleplay import GooglePlayAPI
from .models import *


@shared_task
def download_app_from_playstore(*args, **kwargs):
    application_id = kwargs['app_id']
    app = get_object_or_None(AppInfo, pk=application_id)
    if app:
        api = GooglePlayAPI(androidId=settings.ANDROID_DEVICE_ID)
        api.login(settings.GOOGLE_LOGIN_ID, settings.GOOGLE_PASSWORD)
        response = api.details(app.package_name)
        doc = response.docV2
        version = doc.details.appDetails.versionCode
        app_name = "%s-%s.apk" % (app.package_name, version)
        apk_file = normpath(join(settings.APPLICATION_DOWNLOAD_ROOT, app_name))

        if not exists(settings.APPLICATION_DOWNLOAD_ROOT):
            makedirs(settings.APPLICATION_DOWNLOAD_ROOT)
        if not exists(apk_file):
            data = api.download(app.package_name, version)
            open(apk_file, "wb").write(data)


@shared_task
def log_appbuddy_install(*args, **kwargs):
    log_data = kwargs['log_data']
    stream = BytesIO(log_data)
    data = JSONParser().parse(stream)
    user = get_object_or_None(AppBuddyUser, device_id=data.get('device_id'))

    if user is None:
        device_id = data.get('device_id')
        print data
        agent = get_object_or_None(AgentInfo, agent_id=data.get('agent_id'))
        location = agent.location
        device_info = get_object_or_None(DeviceInfo, box_identifier=data.get('device_info_id'))
        imei = data.get('imei', '')
        make = data.get('make', '')
        model = data.get('model', '')
        mac_address = data.get('mac_address', '')
        app_version = data.get('app_version', '')
        os_version = data.get('os_version', '')
        emails = data.get('emails', '')
        phone_number = data.get('phone_number', '')
        packages = data.get('packages')
        user = AppBuddyUser.objects.create(device_id=device_id, imei=imei, mac_address=mac_address, agent_info=agent,
                                   device_info=device_info, location_info=location, make=make, model=model,
                                   app_version=app_version, os_version=os_version, email_address=emails,
                                   phone_number=phone_number, app_packages=packages, install_count=1)
        user.save()
    else:
        user.install_count += 1
        user.save()

