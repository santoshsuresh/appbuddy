from django.conf import settings
from django.core.management import BaseCommand
from buddy.models import AppInfo
# from tasks import download_from_app_store
from buddy.management import downloader
from buddy.playapi.googleplay import GooglePlayAPI
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        apps = AppInfo.objects.filter(active=True)
        packages = []
        api = GooglePlayAPI(androidId=settings.ANDROID_DEVICE_ID)
        api.login(settings.GOOGLE_LOGIN_ID, settings.GOOGLE_PASSWORD)
        for app in apps:
            print "Checking app %s " % app.package_name
            packages.append(app.package_name)
            response = api.details(app.package_name)
            current_version = int(app.app_version)
            version_from_play_store = response.docV2.details.appDetails.versionCode
            existing_file = "%s/%s-%s.apk" % (settings.APPLICATION_DOWNLOAD_ROOT, app.package_name, app.app_version)
            if current_version != version_from_play_store or not os.path.exists(existing_file):
                app.app_version = version_from_play_store
                app.save()
                print "Downloading file: %s " % existing_file
                if os.path.exists(existing_file):
                    os.unlink(existing_file)
                downloader.delay(app_id=app.pk)



