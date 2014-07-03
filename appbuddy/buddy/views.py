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
from .filters import DeviceInfoFilter, CategoryFilter, CityInfoFilter, DataCardFilter
from .forms import DeviceInfoForm, CategoryForm, CityInfoForm, DataCardInfoForm
from .models import *
from .serializers import AppBuddySerializer


class BaseFilterView(LoginRequiredMixin, FilterView):
    header_names = []
    title = ''
    title_singular = ''
    type_name = ''

    def get_context_data(self, **kwargs):
        context = super(BaseFilterView, self).get_context_data(**kwargs)
        context['type_name'] = self.type_name
        context['title'] = self.title
        context['title_singular'] = self.title_singular
        context['headers'] = self.header_names
        return context


class DeviceInfoListView(BaseFilterView):
    model = DeviceInfo
    filterset_class = DeviceInfoFilter
    header_names = ['Device Identifier', 'Device Type', 'City', 'Mac Address', 'Data Card Ref Num',
                    'Location']
    title = 'Hotspots'
    title_singular = 'Hotspot'
    type_name = 'devices'


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


class CategoryListView(BaseFilterView):
    model = Category
    filterset_class = CategoryFilter
    header_names = ['Name']
    title_singular = 'Categories'
    title = 'Category'
    type_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('categories-list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('categories-list')


class CityInfoListView(BaseFilterView):
    model = CityInfo
    filterset_class = CityInfoFilter
    header_names = ['Name']
    title_singular = 'City'
    title = 'Cities'
    type_name = 'cities'


class CityInfoCreateView(LoginRequiredMixin, CreateView):
    model = CityInfo
    form_class = CityInfoForm

    def get_success_url(self):
        return reverse('cities-list')


class CityInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = CityInfo
    form_class = CityInfoForm

    def get_success_url(self):
        return reverse('cities-list')


class DataCardInfoListView(BaseFilterView):
    model = DataCardInfo
    filterset_class = DataCardFilter
    header_names = ['Reference Number','Card Type', 'Mobile Number']
    title_singular = 'Data Card'
    title = 'Data Cards'
    type_name = 'cards'


class DataCardInfoCreateView(LoginRequiredMixin, CreateView):
    model = DataCardInfo
    form_class = DataCardInfoForm

    def get_success_url(self):
        return reverse('cards-list')


class DataCardInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = DataCardInfo
    form_class = DataCardInfoForm

    def get_success_url(self):
        return reverse('cards-list')


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