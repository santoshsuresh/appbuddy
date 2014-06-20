from django.conf.urls import patterns, url, include
from rest_framework import routers
from .api import AppInfoViewSet, CategoryViewSet, PushNotificationViewSet, AgentViewSet, AppBuddyUserViewSet, \
    DeviceInfoViewSet
from .views import AppBuddyUserList

router = routers.DefaultRouter()
router.register('appinfo', AppInfoViewSet)
router.register('category', CategoryViewSet)
router.register('notifier', PushNotificationViewSet)
router.register('agent', AgentViewSet)
router.register('logUser', AppBuddyUserViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)