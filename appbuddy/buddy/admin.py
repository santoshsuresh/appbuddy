from django.contrib import admin

# Register your models here.
from .models import *


class BaseAdmin(admin.ModelAdmin):
    # date_hierarchy = 'created'
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
    pass


class DeviceInfoAdmin(BaseAdmin):
    pass


class LocationPartnerAdmin(BaseAdmin):
    pass


class LocationInfoAdmin(BaseAdmin):
    pass


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
admin.site.register(DataCardInfo, BaseAdmin)
admin.site.register(BusinessPartner, BaseAdmin)