from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django_filters.views import FilterView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import DeviceInfoFilter
from .forms import DeviceInfoForm
from .models import AppBuddyUser, DeviceInfo
from .serializers import AppBuddySerializer


class DeviceInfoListView(LoginRequiredMixin, FilterView):
    model = DeviceInfo
    filterset_class = DeviceInfoFilter
    context_object_name = 'devices'


class DeviceInfoCreateView(LoginRequiredMixin, CreateView):
    model = DeviceInfo
    form_class = DeviceInfoForm

    def get_success_url(self):
        return reverse('devices-list')


class DeviceInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = DeviceInfo
    form_class = DeviceInfoForm

    def get_success_url(self):
        return reverse('devices-list')




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
            # send it to celery for processing
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)