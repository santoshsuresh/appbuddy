from django.conf import settings
from django.db.models import signals
from django.core.mail import send_mail
from django.db import models
from django_hstore import hstore
from model_utils import Choices
from model_utils.models import TimeStampedModel
from .playapi.googleplay import GooglePlayAPI


class CityInfo(TimeStampedModel):
    name = models.CharField(max_length=100);


class DeviceInfo(TimeStampedModel):
    TYPE_CHOICES = Choices(('BuzzBox', 'Buzz Box'), ('tplink', 'TP Link 3020'))
    boxIdentifier = models.IntegerField()
    deviceType = models.CharField(max_length=20, choices=TYPE_CHOICES, default='tplink')
    city = models.ForeignKey(CityInfo, related_name='devices')


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
        print(doc.details.appDetails)
        print(doc.details)
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
    city = models.ForeignKey(CityInfo, related_name='agents')
    state = models.CharField(max_length=50, default='Karnataka')
    pinCode = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    agentId = models.PositiveIntegerField(blank=True, null=True, default=None)
    photograph = models.ImageField(upload_to='agent_pictures', blank=True, null=True)
    validatedOn = models.DateTimeField(blank=True, null=True, default=None)


    def generate(self):
        # should generate an agent id
        pass


class LocationPartner(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    mobileNumber = models.CharField(max_length=20, unique=True)
    city = models.ForeignKey(CityInfo, related_name='partners')
    numberOfStores = models.PositiveIntegerField()


class LocationInfo(TimeStampedModel):
    DAY_CHOICES = Choices(('all', 'All Days'), ('weekdays', 'Week Days'), ('weekends', 'WeekEnds'))
    TIME_CHOICES = Choices(('all', 'All Times'), ('morning', 'Mornings'), ('evening', 'Evenings'), ('night', 'Night'))
    name = models.CharField(max_length=100)
    partner = models.ForeignKey(LocationPartner, related_name="stores")
    address = models.TextField()
    footFall = models.PositiveIntegerField(default=0)
    area = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(CityInfo, related_name='locations')
    landlineNumber = models.CharField(max_length=20, blank=True, null=True)
    storeManagerName = models.CharField(max_length=100)
    storeManagerNumber = models.CharField(max_length=20)
    preferredDays = models.CharField(max_length=20, choices=DAY_CHOICES, default='all')
    preferredTime = models.CharField(max_length=20, choices=TIME_CHOICES, default='all')
    deviceInfo = models.ForeignKey(DeviceInfo, related_name='locations')
    agent = models.ForeignKey(AgentInfo, related_name='locations')


class AppBuddyUser(TimeStampedModel):
    deviceId = models.CharField(max_length=32)
    imei = models.CharField(max_length=32)
    macAddress = models.CharField(max_length=32)
    agentInfo = models.ForeignKey(AgentInfo)
    deviceInfo = models.ForeignKey(DeviceInfo)
    locationInfo = models.ForeignKey(LocationInfo)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    appVersion = models.CharField(max_length=50)
    osVersion = models.CharField(max_length=50)
    emailAddress = hstore.DictionaryField()
    phoneNumber = models.CharField(max_length=50)
    app_packages = hstore.DictionaryField()

    objects = hstore.HStoreManager()


class DownloadLog(TimeStampedModel):
    STATUS_CHOICES = Choices(('installing', 'Installing'), ('installed', 'Installed'), ('opened', 'Opened'),
                             ('reinstalled', 'Reinstalled'))
    userInfo = models.ForeignKey(AppBuddyUser, related_name='downloads')
    deviceInfo = models.ForeignKey(DeviceInfo, related_name='downloads')
    agentInfo = models.ForeignKey(DeviceInfo, related_name='downloads')
    ipAddress = models.CharField(max_length=20)
    locationInfo = models.ForeignKey(LocationInfo, related_name='downloads')
    version = models.CharField(max_length=20)
    appInfo = models.ForeignKey(AppInfo, related_name='downloads')
    appName = models.CharField(max_length=200)
    packageName = models.CharField(max_length=200)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='installing')
    operator = models.CharField(max_length=50, default=None, blank=True, null=True)
    emailAddress = models.EmailField()

    


signals.post_save.connect(do_on_agent_save, sender=AgentInfo)
