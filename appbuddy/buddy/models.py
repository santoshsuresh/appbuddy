from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.mail import send_mail
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel
from .playapi.googleplay import GooglePlayAPI


MOBILE_CHOICES = Choices(('android', 'Android'), ('iOS', 'iOS'), ('others', 'Others'))


class CityInfo(TimeStampedModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return self.name


class DataCardInfo(TimeStampedModel):
    CARD_CHOICES = Choices(('photon', 'Tata Photon'), ('airtel', 'Airtel'), ('mts', 'MTS'), ('reliance', 'Reliance'))
    card_type = models.CharField(max_length=10, choices=CARD_CHOICES)
    reference_number = models.CharField(max_length=30, unique=True)
    mobile_number = models.CharField(max_length=30, default=None, blank=True, null=True)

    def __unicode__(self):
        return "%s (%s)" % (self.card_type, self.reference_number)


class DeviceInfo(TimeStampedModel):
    TYPE_CHOICES = Choices(('BuzzBox', 'Buzz Box'), ('tplink', 'TP Link 3020'))
    box_identifier = models.IntegerField(verbose_name='Hotspot ID (HID)', unique=True)
    device_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='tplink')
    city = models.ForeignKey(CityInfo, related_name='devices')
    mac_address = models.CharField(max_length=20, verbose_name='Device Mac Address')
    card_info = models.OneToOneField('DataCardInfo', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Appbuddy Device'
        verbose_name_plural = 'Appbuddy Devices'

    def __unicode__(self):
        return "%s (%s)" % (self.box_identifier, self.city)


class PushNotificatonRegistration(TimeStampedModel):
    unique_id = models.CharField(max_length=100)
    device_type = models.CharField(choices=MOBILE_CHOICES, max_length=20, default='android')
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

    class Meta:
        verbose_name = 'Push Notification Registration'
        verbose_name_plural = 'Push Notification Registrations'


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    where_clause = models.CharField(max_length=100, default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class WhitelistUrl(TimeStampedModel):
    TYPE_CHOICES = Choices(('proxy', 'Proxy'), ('dns', 'DNS'))
    url = models.CharField(max_length=100)
    type = models.CharField(max_length=10, default='proxy', choices=TYPE_CHOICES)

    def __unicode__(self):
        return "%s (%s)" % (self.url, self.type)


class AppInfo(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    package_name = models.CharField(max_length=100)
    market_url = models.CharField(max_length=255)
    download_time_wifi = models.PositiveIntegerField(default=0)
    download_time_3g = models.PositiveIntegerField(default=0)
    download_time_edge = models.PositiveIntegerField(default=0)
    active = models.BooleanField()
    open_on_install = models.BooleanField(default=True)
    app_version = models.CharField(max_length=50, default=None, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails')
    categories = models.ManyToManyField(to=Category)
    min_android_version = models.CharField(max_length=10, default=14)
    cities = models.ManyToManyField('CityInfo', related_name='apps', )
    whitelisted_urls = models.ManyToManyField('WhitelistUrl', related_name='apps')
    download_size = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def _get_app_version_from_playstore(self):
        api = GooglePlayAPI(androidId=settings.ANDROID_DEVICE_ID)
        api.login(settings.GOOGLE_LOGIN_ID, settings.GOOGLE_PASSWORD)
        response = api.details(self.package_name)
        doc = response.docV2
        self.download_size = doc.details.appDetails.installationSize
        self.app_version = doc.details.appDetails.versionCode

    def save(self, *args, **kwargs):
        self._get_app_version_from_playstore()
        super(AppInfo, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


def do_on_agent_save(sender, instance, created, **kwargs):
    send_mail('Agent Created', 'Here is the message', 'appbuddy@telibrahma.com',
              ['santosh.s@telibrahma.com', 'vinay.jayaram@telibrahma.com'], fail_silently=False)


class AgentInfo(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    mobile_number = models.CharField(max_length=20, unique=True)
    city = models.ForeignKey(CityInfo, related_name='agents')
    state = models.CharField(max_length=50, default='Karnataka')
    pin_code = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    agent_id = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(20000), MaxValueValidator(35000)],
                                           verbose_name='Agent Code')
    photograph = models.ImageField(upload_to='agent_pictures', blank=True, null=True)
    validated_on = models.DateTimeField(blank=True, null=True, default=None)
    mobile_os = models.CharField(max_length=20, default=None, blank=True, null=True, choices=MOBILE_CHOICES)
    make = models.CharField(max_length=50, default=None, blank=True, null=True)
    model = models.CharField(max_length=50, default=None, blank=True, null=True)


    class Meta:
        verbose_name = 'Promoter'
        verbose_name_plural = 'Promoters'


    def __unicode__(self):
        return self.name


class BusinessPartner(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    mobile_number = models.CharField(max_length=20, unique=True)
    city = models.ForeignKey(CityInfo, related_name='business_partners')
    description = models.TextField(default=None, blank=True, null=True)

    def __unicode__(self):
        return self.name


class LocationPartner(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    mobile_number = models.CharField(max_length=20, unique=True)
    city = models.ForeignKey(CityInfo, related_name='partners')
    number_of_stores = models.PositiveIntegerField()
    businessPartner = models.ForeignKey('BusinessPartner', related_name='location_partners')

    class Meta:
        verbose_name = 'Location Partner'
        verbose_name_plural = 'Location Partners'


    def __unicode__(self):
        return self.name


class LocationInfo(TimeStampedModel):
    DAY_CHOICES = Choices(('all', 'All Days'), ('weekdays', 'Week Days'), ('weekends', 'WeekEnds'))
    TIME_CHOICES = Choices(('all', 'All Times'), ('morning', 'Mornings'), ('evening', 'Evenings'), ('night', 'Night'))
    name = models.CharField(max_length=100)
    partner = models.ForeignKey(LocationPartner, related_name="stores")
    address = models.TextField()
    foot_fall = models.PositiveIntegerField(default=0)
    area = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(CityInfo, related_name='locations')
    landline_number = models.CharField(max_length=20, blank=True, null=True)
    store_manager_name = models.CharField(max_length=100)
    store_manager_number = models.CharField(max_length=20)
    preferred_days = models.CharField(max_length=20, choices=DAY_CHOICES, default='all')
    preferred_time = models.CharField(max_length=20, choices=TIME_CHOICES, default='all')
    device_info = models.OneToOneField(DeviceInfo, related_name='locations', default=None, blank=True, null=True)
    agent = models.OneToOneField(AgentInfo, related_name='locations', default=None, blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, default=None, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, default=None, decimal_places=8, blank=True, null=True)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(LocationInfo, self).save(*args, **kwargs)


class AppBuddyUser(TimeStampedModel):
    device_id = models.CharField(max_length=32)
    imei = models.CharField(max_length=32)
    mac_address = models.CharField(max_length=32)
    agent_info = models.ForeignKey(AgentInfo)
    device_info = models.ForeignKey(DeviceInfo)
    location_info = models.ForeignKey(LocationInfo, default=None)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    app_version = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50)
    email_address = models.TextField()
    phone_number = models.CharField(max_length=50)
    app_packages = models.TextField()
    install_count = models.IntegerField(default=0)


    class Meta:
        verbose_name = 'Appbuddy User'
        verbose_name_plural = 'Appbuddy Users'


class DownloadLog(TimeStampedModel):
    STATUS_CHOICES = Choices(('installing', 'Installing'), ('installed', 'Installed'), ('opened', 'Opened'),
                             ('reinstalled', 'Reinstalled'))
    user_info = models.ForeignKey(AppBuddyUser, related_name='downloads')
    device_info = models.ForeignKey(DeviceInfo, related_name='installs')
    agent_info = models.ForeignKey(DeviceInfo, related_name='downloads')
    ip_address = models.CharField(max_length=20)
    location_info = models.ForeignKey(LocationInfo, related_name='downloads')
    version = models.CharField(max_length=20)
    app_info = models.ForeignKey(AppInfo, related_name='downloads')
    app_name = models.CharField(max_length=200)
    package_name = models.CharField(max_length=200)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='installing')
    operator = models.CharField(max_length=50, default=None, blank=True, null=True)
    email_address = models.EmailField()