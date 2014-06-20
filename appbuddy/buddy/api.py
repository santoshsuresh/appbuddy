from rest_framework import viewsets,status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import AppBuddySerializer
from .models import AppInfo, Category, PushNotificatonRegistration, AgentInfo, AppBuddyUser, DeviceInfo


class PushNotificationViewSet(viewsets.ModelViewSet):
    model = PushNotificatonRegistration


class AppInfoViewSet(viewsets.ModelViewSet):
    model = AppInfo


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category


class AgentViewSet(viewsets.ModelViewSet):
    model = AgentInfo


class AppBuddyUserViewSet(viewsets.ModelViewSet):
    model = AppBuddyUser
    serializer_class = AppBuddySerializer

    def list(self, request, *args, **kwargs):
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = AppBuddySerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            json = JSONRenderer().render(serializer.data)
            print json
            return Response(None, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceInfoViewSet(viewsets.ModelViewSet):
    model = DeviceInfo

