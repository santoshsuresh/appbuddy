from django.conf.urls import patterns, url, include
from rest_framework import routers
from .api import AppInfoViewSet, CategoryViewSet, PushNotificationViewSet, AgentViewSet

router = routers.DefaultRouter()
router.register('appinfo', AppInfoViewSet)
router.register('category', CategoryViewSet)
router.register('notifier', PushNotificationViewSet)
router.register('agent', AgentViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)