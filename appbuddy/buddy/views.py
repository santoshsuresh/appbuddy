from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView
from django_filters.views import FilterView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import DeviceInfoFilter, CategoryFilter, CityInfoFilter, DataCardFilter, BusinessPartnerFilter
from .forms import DeviceInfoForm, CategoryForm, CityInfoForm, DataCardInfoForm, BusinessPartnerCreationForm, \
    BusinessPartnerChangeForm, LocationPartnerCreationForm, LocationPartnerChangeForm
from .models import *
from .serializers import AppBuddySerializer


class SuperuserRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(SuperuserRequiredMixin, self).dispatch(*args, **kwargs)


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


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'bracket.html'


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
    header_names = ['Reference Number', 'Card Type', 'Mobile Number']
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


class BusinessPartnerListView(BaseFilterView):
    header_names = ['Email Address', 'first_name', 'last_name', 'mobile_number', 'city']
    filterset_class = BusinessPartnerFilter
    title = 'Business Partners'
    title_singular = 'Business Partner'
    type_name = 'businesspartners'
    model = BusinessPartner


class BusinessPartnerCreateView(LoginRequiredMixin, CreateView):
    model = BusinessPartner
    form_class = BusinessPartnerCreationForm

    def get_success_url(self):
        return reverse('businesspartners-list')

    def get_initial(self):
        return {'type': 'business_partner'}


class BusinessPartnerUpdateView(LoginRequiredMixin, UpdateView):
    model = BusinessPartner
    form_class = BusinessPartnerChangeForm

    def get_success_url(self):
        return reverse('businesspartners-list')

    def get_initial(self):
        return {'type': 'business_partner'}


class LocationPartnerListView(BaseFilterView):
    header_names = ['Email Address', 'first_name', 'last_name', 'mobile_number', 'city']
    filterset_class = BusinessPartnerFilter
    title = 'Location Partners'
    title_singular = 'Location Partner'
    type_name = 'locationpartners'
    model = LocationPartner

    def get_queryset(self):
        if self.request.user.is_superuser:
            return LocationPartner.objects.all()
        elif self.request.user.type == 'business_partner':
            return LocationPartner.objects.filter(business_partner=self.request.user)
        return LocationPartner.objects.all()


class LocationPartnerCreateView(LoginRequiredMixin, CreateView):
    model = LocationPartner
    form_class = LocationPartnerCreationForm

    def get_success_url(self):
        return reverse('locationpartners-list')

    def get_initial(self):
        return {'type': 'location_partner', 'business_partner': self.request.user}


class LocationPartnerUpdateView(LoginRequiredMixin, UpdateView):
    model = LocationPartner
    form_class = LocationPartnerChangeForm

    def get_success_url(self):
        return reverse('locationpartners-list')

    def get_initial(self):
        return {'type': 'location_partner', 'business_partner': self.request.user}



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