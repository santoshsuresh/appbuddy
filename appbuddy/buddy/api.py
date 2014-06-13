from rest_framework import viewsets
from .models import AppInfo, Category, PushNotificatonRegistration


class PushNotificationViewSet(viewsets.ModelViewSet):
    model = PushNotificatonRegistration


class AppInfoViewSet(viewsets.ModelViewSet):
    model = AppInfo


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category