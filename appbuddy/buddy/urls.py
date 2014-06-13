from django.conf.urls import patterns, url, include
from rest_framework import routers
from .api import AppInfoViewSet, CategoryViewSet, PushNotificationViewSet

router = routers.DefaultRouter()
router.register('appinfo', AppInfoViewSet)
router.register('category', CategoryViewSet)
router.register('notifier', PushNotificationViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)