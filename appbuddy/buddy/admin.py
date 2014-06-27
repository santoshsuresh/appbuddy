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
    list_display = (
        'name', 'active', 'package_name', 'open_on_install', 'app_version', 'min_android_version', 'download_in_mb')
    list_filter = ('active', 'open_on_install')
    filter_horizontal = ('cities', 'categories', 'whitelisted_urls')

    def download_in_mb(self, obj):
        if obj.download_size > 0:
            return "%.2f MB" % (obj.download_size / 1024.0 / 1024.0)
        return "0 MB"
    download_in_mb.short_description = 'Download Size (MB)'


class AgentInfoAdmin(BaseAdmin):
    list_display = ('name', 'email', 'agent_id', 'mobile_number', 'city', 'active', 'locations')
    list_filter = ('active', 'city__name', 'locations__partner__name')
    pass


class DeviceInfoAdmin(BaseAdmin):
    list_display = ('box_identifier', 'device_type', 'city')
    pass


class LocationPartnerAdmin(BaseAdmin):
    list_display = ('name', 'email', 'mobile_number', 'city')
    pass


class LocationInfoAdmin(BaseAdmin):
    list_display = ('name', 'partner', 'city', 'agent')
    list_filter = ('city__name', 'device_info__device_type', 'partner__name' )


class WhitelistUrlAdmin(BaseAdmin):
    list_display = ('url', 'type')
    list_filter = ('type', )


admin.site.register(PushNotificatonRegistration, PushNotificationRegistrationAdmin)
admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AgentInfo, AgentInfoAdmin)
admin.site.register(AppBuddyUser, BaseAdmin)
admin.site.register(LocationPartner, LocationPartnerAdmin)
admin.site.register(LocationInfo, LocationInfoAdmin)
admin.site.register(CityInfo, BaseAdmin)
admin.site.register(DeviceInfo, DeviceInfoAdmin)
admin.site.register(WhitelistUrl, WhitelistUrlAdmin)