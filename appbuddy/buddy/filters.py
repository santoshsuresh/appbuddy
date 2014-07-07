from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import template
from django.forms import ModelChoiceField
from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from .models import DeviceInfo, Category, CityInfo, DataCardInfo, BusinessPartner, LocationInfo, LocationPartner


class DeviceInfoFilter(FilterSet):
    class Meta:
        model = DeviceInfo
        fields = ['city', 'box_identifier']
        order_by = ['box_identifier', 'city']

    def __init__(self, *args, **kwargs):
        super(DeviceInfoFilter, self).__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form-inline'
        helper.field_template = 'bootstrap3/layout/inline_field.html'
        helper.layout = Layout(
            'box_identifier',
            'city',
            Submit('submit', 'Filter', css_class='btn-primary'),
        )
        self.form.helper = helper


class CategoryFilter(FilterSet):
    name = CharFilter(lookup_type='icontains')

    class Meta:
        model = Category
        fields = ['name']
        order_by = ['name']

    def __init__(self, *args, **kwargs):
        super(CategoryFilter, self).__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form-inline'
        helper.field_template = 'bootstrap3/layout/inline_field.html'
        helper.layout = Layout(
            'name',
            Submit('submit', 'Filter', css_class='btn-primary'),
        )
        self.form.helper = helper


class CityInfoFilter(FilterSet):
    name = CharFilter(lookup_type='icontains')

    class Meta:
        model = CityInfo
        fields = ['name']
        order_by = ['name']

    def __init__(self, *args, **kwargs):
        super(CityInfoFilter, self).__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form-inline'
        helper.field_template = 'bootstrap3/layout/inline_field.html'
        helper.layout = Layout(
            'name',
            Submit('submit', 'Filter', css_class='btn-primary'),
        )
        self.form.helper = helper


class DataCardFilter(FilterSet):
    reference_number = CharFilter(lookup_type='icontains')

    class Meta:
        model = DataCardInfo
        fields = ['card_type', 'reference_number']

    def __init__(self, *args, **kwargs):
        super(DataCardFilter, self).__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form-inline'
        helper.field_template = 'bootstrap3/layout/inline_field.html'
        helper.layout = Layout(
            'card_type',
            'reference_number',
            Submit('submit', 'Filter', css_class='btn-primary'),
        )
        self.form.helper = helper

class BusinessPartnerFilter(FilterSet):
    email = CharFilter(lookup_type='icontains')
    mobile_number = CharFilter(lookup_type='icontains')

    class Meta:
        model = BusinessPartner
        fields = ['email', 'mobile_number', 'city']

    def __init__(self, *args, **kwargs):
        super(BusinessPartnerFilter, self).__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form-inline'
        helper.field_template = 'bootstrap3/layout/inline_field.html'
        helper.layout = Layout(
            'email',
            'mobile_number',
            'city',
            Submit('submit', 'Filter', css_class='btn-primary'),
        )
        self.form.helper = helper


class LocationInfoFilter(FilterSet):
    class Meta:
        model = LocationInfo
        fields = ['partner', 'city']

    def __init__(self, *args, **kwargs):
        super(LocationInfoFilter, self).__init__(*args, **kwargs)
        helper = FormHelper()
        helper.form_class = 'form-inline'
        helper.field_template = 'bootstrap3/layout/inline_field.html'
        helper.layout = Layout(
            'partner',
            'city',
            Submit('submit', 'Filter', css_class='btn-primary'),
        )
        self.form.helper = helper

