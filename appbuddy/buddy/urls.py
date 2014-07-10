from django.conf.urls import patterns, url, include
from rest_framework import routers
from .api import AppInfoViewSet, CategoryViewSet, PushNotificationViewSet, AgentViewSet, AppBuddyUserViewSet, \
    DeviceInfoViewSet, CityInfoViewSet, WhitelistUrlViewSet
from .views import *

router = routers.DefaultRouter()
router.register('appinfo', AppInfoViewSet)
router.register('category', CategoryViewSet)
router.register('notifier', PushNotificationViewSet)
router.register('agent', AgentViewSet)
router.register('logUser', AppBuddyUserViewSet)
router.register('cities', CityInfoViewSet)
router.register('urls', WhitelistUrlViewSet)


urlpatterns = patterns('',
    url(r'^api/v1/', include(router.urls)),

    url(r'^devices/$', DeviceInfoListView.as_view(),name='devices-list'),
    url(r'^devices/add/$', DeviceInfoCreateView.as_view(), name='devices-create'),
    url(r'^devices/edit/(?P<pk>\d+)$', DeviceInfoUpdateView.as_view(), name='devices-edit'),

    url(r'^categories/$', CategoryListView.as_view(),name='categories-list'),
    url(r'^categories/add/$', CategoryCreateView.as_view(),name='categories-create'),
    url(r'^categories/edit/(?P<pk>\d+)$', CategoryUpdateView.as_view(),name='categories-edit'),

    url(r'^cities/$', CityInfoListView.as_view(),name='cities-list'),
    url(r'^cities/add/$', CityInfoCreateView.as_view(),name='cities-create'),
    url(r'^cities/edit/(?P<pk>\d+)$', CityInfoUpdateView.as_view(),name='cities-edit'),

    url(r'^cards/$', DataCardInfoListView.as_view(),name='cards-list'),
    url(r'^cards/add/$', DataCardInfoCreateView.as_view(),name='cards-create'),
    url(r'^cards/edit/(?P<pk>\d+)$', DataCardInfoUpdateView.as_view(),name='cards-edit'),


    url(r'^businesspartners/$', BusinessPartnerListView.as_view(),name='businesspartners-list'),
    url(r'^businesspartners/add/$', BusinessPartnerCreateView.as_view(),name='businesspartners-create'),
    url(r'^businesspartners/edit/(?P<pk>\d+)$', BusinessPartnerUpdateView.as_view(),name='businesspartners-edit'),

    url(r'^locationpartners/$', LocationPartnerListView.as_view(),name='locationpartners-list'),
    url(r'^locationpartners/add/$', LocationPartnerCreateView.as_view(),name='locationpartners-create'),
    url(r'^locationpartners/edit/(?P<pk>\d+)$', LocationPartnerUpdateView.as_view(),name='locationpartners-edit'),

    url(r'^agent/$', AgentInfoListView.as_view(),name='agent-list'),
    url(r'^agent/add/$', AgentInfoCreateView.as_view(),name='agent-create'),
    url(r'^agent/edit/(?P<pk>\d+)$', AgentInfoUpdateView.as_view(),name='agent-edit'),

    url(r'^locations/$', LocationListView.as_view(),name='locations-list'),
    url(r'^locations/unassigned$', UnassignedLocationListView.as_view(),name='unassigned-list'),
    url(r'^locations/add/$', LocationCreateView.as_view(),name='locations-create'),
    url(r'^locations/edit/(?P<pk>\d+)$', LocationUpdateView.as_view(),name='locations-edit'),

    url(r'^applications/$', AppInfoListView.as_view(),name='applications-list'),
    url(r'^applications/add/$', AppInfoCreateView.as_view(),name='applications-create'),
    url(r'^applications/edit/(?P<pk>\d+)$', AppInfoUpdateView.as_view(),name='applications-edit'),

    url(r'^locations/assign/(?P<pk>\d+)$', LocationAssignView.as_view(), name='assign-location')



)