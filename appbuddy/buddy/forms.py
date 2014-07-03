from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from .models import DeviceInfo


class DeviceInfoForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = DeviceInfo