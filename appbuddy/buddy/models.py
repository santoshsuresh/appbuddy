from django.conf import settings
from django.db.models import signals
from django.core.mail import send_mail
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel
from .playapi.googleplay import GooglePlayAPI


class PushNotificatonRegistration(TimeStampedModel):
    TYPE_CHOICES = Choices(('android', 'Android'), ('iOS', 'iOS'))
    unique_id = models.CharField(max_length=100)
    device_type = models.CharField(choices=TYPE_CHOICES, max_length=20, default='android')
    registration_id = models.CharField(max_length=255)
    app_version = models.CharField(max_length=10)
    os_version = models.CharField(max_length=10, default=None, blank=True, null=True)
    make = models.CharField(max_length=100, default=None, blank=True)
    model = models.CharField(max_length=100, default=None, blank=True)
    imei = models.CharField(max_length=100, default=None, blank=True)
    phone_number = models.CharField(max_length=100, default=None, blank=True)
    screen_width = models.PositiveIntegerField(default=0)
    screen_height = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    where_clause = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __unicode__(self):
        return self.name


class AppInfo(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    package_name = models.CharField(max_length=100)
    market_url = models.CharField(max_length=255)
    download_time_wifi = models.PositiveIntegerField()
    download_time_3g = models.PositiveIntegerField()
    download_time_edge = models.PositiveIntegerField()
    active = models.BooleanField()
    open_on_install = models.BooleanField(default=True)
    app_version = models.CharField(max_length=50, default=None, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails')
    categories = models.ManyToManyField(to=Category)
    min_android_version = models.CharField(max_length=10)

    def _get_app_version_from_playstore(self):
        api = GooglePlayAPI(androidId=settings.ANDROID_DEVICE_ID)
        api.login(settings.GOOGLE_LOGIN_ID, settings.GOOGLE_PASSWORD)
        response = api.details(self.package_name)
        doc = response.docV2
        self.app_version = doc.details.appDetails.versionCode

    def save(self, *args, **kwargs):
        self._get_app_version_from_playstore()
        super(AppInfo, self).save(*args, **kwargs)


def do_on_agent_save(sender, instance, created, **kwargs):
    send_mail('Agent Created', 'Here is the message', 'appbuddy@telibrahma.com',
              ['santosh.s@telibrahma.com', 'vinay.jayaram@telibrahma.com'], fail_silently=False)


class AgentInfo(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    mobileNumber = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default='Karnataka')
    pinCode = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    agentId = models.PositiveIntegerField(blank=True, null=True)
    photograph = models.ImageField(upload_to='agent_pictures', blank=True, null=True)
    validatedOn = models.DateTimeField(blank=True, null=True)


    def generate(self):
        # should generate an agent id
        pass


signals.post_save.connect(do_on_agent_save, sender=AgentInfo)
