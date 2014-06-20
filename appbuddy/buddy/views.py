from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AppBuddyUser
from .serializers import AppBuddySerializer


class AppBuddyUserList(APIView):

    model = AppBuddyUser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        logs = AppBuddyUser.objects.all()
        serializer = AppBuddySerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppBuddySerializer(data=request.DATA)
        if serializer.is_valid():
            #send it to celery for processing
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)