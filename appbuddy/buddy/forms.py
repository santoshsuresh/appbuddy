from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, ButtonHolder, HTML
from django.forms import ModelForm
from .models import DeviceInfo, Category, CityInfo, DataCardInfo


class DeviceInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeviceInfoForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['box_identifier'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            'box_identifier',
            'device_type',
            'city',
            'mac_address',
            'card_info',
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'devices-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = DeviceInfo


class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            'name',
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'categories-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = Category


class CityInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CityInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            'name',
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'cities-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = CityInfo

class DataCardInfoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DataCardInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            'card_type',
            'reference_number',
            'mobile_number',
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'cards-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = DataCardInfo

