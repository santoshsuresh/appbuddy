from rest_framework import serializers
from .models import AppInfo


class AppInfoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = AppInfo



