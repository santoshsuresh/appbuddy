from rest_framework import serializers
from .models import AppInfo, AppBuddyUser


class AppInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppInfo


class AppBuddySerializer(serializers.ModelSerializer):
    agent_id = serializers.IntegerField()
    device_info_id = serializers.IntegerField()
    emails = serializers.CharField()
    packages = serializers.CharField()

    class Meta:
        model = AppBuddyUser
        fields = (
            'device_id', 'imei', 'mac_address', 'device_info_id', 'agent_id', 'make', 'model', 'app_version', 'os_version',
            'emails', 'phone_number', 'packages')


