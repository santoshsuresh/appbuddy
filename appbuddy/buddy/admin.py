from django.contrib import admin

# Register your models here.
from .models import PushNotificatonRegistration, AppInfo, Category, AgentInfo


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