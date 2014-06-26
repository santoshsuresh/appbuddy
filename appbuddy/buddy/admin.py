from django.contrib import admin

# Register your models here.
from .models import *


class BaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    pass


class CategoryAdmin(BaseAdmin):
    pass


class PushNotificationRegistrationAdmin(BaseAdmin):
    pass


class AppInfoAdmin(BaseAdmin):
    list_display = ('name', 'active', 'package_name', 'open_on_install', 'app_version', 'min_android_version')
    list_filter = ('active', 'open_on_install')
    pass


class AgentInfoAdmin(BaseAdmin):
    list_display = ('name', 'email', 'agent_id', 'mobile_number', 'city', 'active', 'locations')
    pass


class DeviceInfoAdmin(BaseAdmin):
    list_display = ('box_identifier', 'device_type', 'city')
    pass


class LocationPartnerAdmin(BaseAdmin):
    list_display = ('name', 'email', 'mobile_number', 'city')
    pass


class LocationInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'partner', 'city', 'agent')
    list_filter = ('city__name', 'device_info__device_type', 'partner__name' )
    pass


admin.site.register(PushNotificatonRegistration, PushNotificationRegistrationAdmin)
admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AgentInfo, AgentInfoAdmin)
admin.site.register(AppBuddyUser, BaseAdmin)
admin.site.register(LocationPartner, LocationPartnerAdmin)
admin.site.register(LocationInfo, LocationInfoAdmin)
admin.site.register(CityInfo, BaseAdmin)
admin.site.register(DeviceInfo, DeviceInfoAdmin)