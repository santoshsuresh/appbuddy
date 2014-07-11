from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse

# Create your views here.
from django.db.models import Q
from django.forms.models import modelformset_factory
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, TemplateView
from django_filters.views import FilterView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import DeviceInfoFilter, CategoryFilter, CityInfoFilter, DataCardFilter, BusinessPartnerFilter, \
    LocationInfoFilter, AgentInfoFilter, AppInfoFilter
from .forms import DeviceInfoForm, CategoryForm, CityInfoForm, DataCardInfoForm, BusinessPartnerCreationForm, \
    BusinessPartnerChangeForm, LocationPartnerCreationForm, LocationPartnerChangeForm, LocationInfoForm, \
    AgentInfoCreationForm, AgentInfoChangeForm, AppInfoForm, LocationAssignForm
from .models import *
from .serializers import AppBuddySerializer, DownloadLogSerializer


class SuperuserRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(SuperuserRequiredMixin, self).dispatch(*args, **kwargs)


# @csrf_exempt
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


class AppInfoListView(BaseFilterView):
    model = AppInfo
    filterset_class = AppInfoFilter
    header_names = ['Name', 'Package Name', 'App Version', 'Download Size', 'Active']
    title = 'Applications'
    title_singular = 'Application'
    type_name = 'applications'


class AppInfoCreateView(LoginRequiredMixin, CreateView):
    model = AppInfo
    form_class = AppInfoForm

    def get_success_url(self):
        return reverse('applications-list')


class AppInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = AppInfo
    form_class = AppInfoForm

    def get_success_url(self):
        return reverse('applications-list')


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
    header_names = ['Email Address', 'First Name', 'Last Name', 'Mobile Number', 'City']
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
    header_names = ['Email Address', 'First Name', 'Last Name', 'Mobile Number', 'City']
    filterset_class = BusinessPartnerFilter
    title = 'Location Partners'
    title_singular = 'Location Partner'
    type_name = 'locationpartners'
    model = LocationPartner

    def get_queryset(self):
        if not self.request.user.is_superuser:
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


class AgentInfoListView(BaseFilterView):
    model = AgentInfo
    filterset_class = AgentInfoFilter
    title = 'Promoter'
    title_singular = 'Promoters'
    type_name = 'agent'
    header_names = ['Agent Code', 'Name', 'City', 'Mobile Number', 'Location Assigned']

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return AgentInfo.objects.filter(business_partner=self.request.user)
        return AgentInfo.objects.all()

    def get_context_data(self, **kwargs):
        if not self.request.user.is_superuser:
            self.filterset.form.fields['location__partner'].queryset = LocationPartner.objects.filter(
                business_partner=self.request.user)
        else:
            self.filterset.form.fields['location__partner'].queryset = LocationPartner.objects.all()
        return super(AgentInfoListView, self).get_context_data(**kwargs)


class AgentInfoCreateView(LoginRequiredMixin, CreateView):
    model = AgentInfo
    form_class = AgentInfoCreationForm

    def get_success_url(self):
        return reverse('agent-list')

    def get_initial(self):
        return {'type': 'agent', 'business_partner': self.request.user}


class AgentInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = AgentInfo
    form_class = AgentInfoChangeForm

    def get_success_url(self):
        return reverse('agent-list')

    def get_initial(self):
        return {'type': 'agent', 'business_partner': self.request.user}


class LocationListView(BaseFilterView):
    model = LocationInfo
    filterset_class = LocationInfoFilter
    title = 'Location'
    title_singular = 'Locations'
    type_name = 'locations'
    header_names = ['Name', 'Partner', 'City', 'Store Manager Name', 'Device', 'Agent']

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return LocationInfo.objects.filter(partner__business_partner=self.request.user)
        return LocationInfo.objects.all()

    def get_context_data(self, **kwargs):
        if not self.request.user.is_superuser:
            self.filterset.form.fields['partner'].queryset = LocationPartner.objects.filter(
                business_partner=self.request.user)
        else:
            self.filterset.form.fields['partner'].queryset = LocationPartner.objects.all()
        return super(LocationListView, self).get_context_data(**kwargs)


class UnassignedLocationListView(LocationListView):
    def get_queryset(self):
        queryset = super(UnassignedLocationListView, self).get_queryset();
        return queryset.filter(Q(device_info__isnull=True) | Q(agent__isnull=True))


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = LocationInfo
    form_class = LocationInfoForm

    def get_form(self, form_class):
        form = super(LocationCreateView, self).get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['partner'].queryset = LocationPartner.objects.filter(Q(business_partner=self.request.user))
        return form

    def get_success_url(self):
        return reverse('locations-list')


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = LocationInfo
    form_class = LocationInfoForm

    def get_form(self, form_class):
        form = super(LocationUpdateView, self).get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['partner'].queryset = LocationPartner.objects.filter(Q(business_partner=self.request.user))
        return form

    def get_success_url(self):
        return reverse('locations-list')


class LocationAssignView(LoginRequiredMixin, UpdateView):
    model = LocationInfo
    form_class = LocationAssignForm

    def get_form(self, form_class):
        form = super(LocationAssignView, self).get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['agent'].queryset = AgentInfo.objects.filter(Q(business_partner=self.request.user))
        return form

    def get_success_url(self):
        return reverse('locations-list')