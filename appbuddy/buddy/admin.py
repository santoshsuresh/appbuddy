from django.contrib import admin

# Register your models here.
from .models import *


class BaseAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(BaseAdmin):
    pass

class PushNotificationRegistrationAdmin(BaseAdmin):
    pass

class AppInfoAdmin(BaseAdmin):
    pass


admin.site.register(PushNotificatonRegistration, PushNotificationRegistrationAdmin)
admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AgentInfo, BaseAdmin)
admin.site.register(AppBuddyUser, BaseAdmin)
admin.site.register(LocationPartner, BaseAdmin)
admin.site.register(LocationInfo, BaseAdmin)
admin.site.register(CityInfo, BaseAdmin)
admin.site.register(DeviceInfo, BaseAdmin)