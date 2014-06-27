from django.conf.urls import patterns, url, include
from rest_framework import routers
from .api import AppInfoViewSet, CategoryViewSet, PushNotificationViewSet, AgentViewSet, AppBuddyUserViewSet, \
    DeviceInfoViewSet, CityInfoViewSet, WhitelistUrlViewSet
from .views import AppBuddyUserList

router = routers.DefaultRouter()
router.register('appinfo', AppInfoViewSet)
router.register('category', CategoryViewSet)
router.register('notifier', PushNotificationViewSet)
router.register('agent', AgentViewSet)
router.register('logUser', AppBuddyUserViewSet)
router.register('cities', CityInfoViewSet)
router.register('urls', WhitelistUrlViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)