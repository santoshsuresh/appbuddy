from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, ButtonHolder, HTML, Field, Fieldset, Hidden
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import DeviceInfo, Category, CityInfo, DataCardInfo, BaseUser, BusinessPartner, LocationPartner, \
    LocationInfo, AgentInfo


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

class LocationInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocationInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            'name',
            'partner',
            Field('address', rows=3),
            'area',
            'city',
            'store_manager_name',
            'store_manager_number',
            'foot_fall',
            'landline_number',
            'preferred_days',
            'preferred_time',
            'latitude',
            'longitude',
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'cards-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = LocationInfo
        exclude = ('device_info', 'agent', )


class BaseUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")

    def clean_email(self):
        email = self.cleaned_data['email']
        if self.instance.pk:
            return email
        try:
            BaseUser._default_manager.get(email=email)
        except BaseUser.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(BaseUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class BusinessPartnerCreationForm(BaseUserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    type = forms.CharField(required=False)


    def __init__(self, *args, **kwargs):
        super(BusinessPartnerCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs['autocomplete'] = 'off'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(

            Fieldset(
                'Authentication Information',
                'email',
                'password1',
                'password2',
            ),
            Fieldset(
                'Personal Info',
                'first_name',
                'last_name',
                'city',
                'mobile_number',
                Field('address', rows=3)
            ),
            HTML("<br/>"),
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'businesspartners-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = BusinessPartner
        exclude = ('username', 'password', 'date_joined', 'last_login')

class AgentInfoCreationForm(BaseUserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True,)
    type = forms.CharField(required=False)
    business_partner = forms.ModelChoiceField(queryset=BusinessPartner.objects.all(), required=False)


    def __init__(self, *args, **kwargs):
        super(AgentInfoCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs['autocomplete'] = 'off'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(

            Fieldset(
                'Authentication Information',
                'email',
                'password1',
                'password2',
                Field('business_partner', type='hidden')
            ),
            Fieldset(
                'Personal Info',
                'first_name',
                'last_name',
                'city',
                'mobile_number',
                Field('address', rows=3)
            ),

            Fieldset(
                'Mobile Information',
                'mobile_os',
                'make',
                'model'
            ),
            HTML("<br/>"),
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'agent-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = AgentInfo
        exclude = ('username', 'password', 'date_joined', 'last_login', 'agent_id')


class LocationPartnerCreationForm(BaseUserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    type = forms.CharField(required=False)
    business_partner = forms.ModelChoiceField(queryset=BusinessPartner.objects.all(), required=False)


    def __init__(self, *args, **kwargs):
        super(LocationPartnerCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs['autocomplete'] = 'off'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset(
                'Authentication Information',
                'email',
                'password1',
                'password2',
                Field('business_partner', type='hidden')
            ),
            Fieldset(
                'Personal Info',
                'first_name',
                'last_name',
                'city',
                'mobile_number',
                Field('address', rows=3)
            ),
            HTML("<br/>"),
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'locationpartners-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = LocationPartner
        exclude = ('username', 'password', 'date_joined', 'last_login', 'baseuser_ptr')


class BusinessPartnerChangeForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    type = forms.CharField(required=False)


    def __init__(self, *args, **kwargs):
        super(BusinessPartnerChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs['autocomplete'] = 'off'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(

            Fieldset(
                'Authentication Information',
                'email',
                'is_active'
            ),
            Fieldset(
                'Personal Info',
                'first_name',
                'last_name',
                'city',
                'mobile_number',
                Field('address', rows=3)
            ),
            HTML("<br/>"),
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'businesspartners-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = BusinessPartner
        exclude = ('username', 'password', 'date_joined', 'last_login', 'password1', 'password2')


class LocationPartnerChangeForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    type = forms.CharField(required=False)
    business_partner = forms.ModelChoiceField(queryset=BusinessPartner.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(LocationPartnerChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs['autocomplete'] = 'off'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(

            Fieldset(
                'Authentication Information',
                'email',
                Field('business_partner', type='hidden'),
                'is_active'
            ),
            Fieldset(
                'Personal Info',
                'first_name',
                'last_name',
                'city',
                'mobile_number',
                Field('address', rows=3)
            ),
            HTML("<br/>"),
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'locationpartners-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = LocationPartner
        exclude = ('username', 'password', 'date_joined', 'last_login', 'password1', 'password2')


class AgentInfoChangeForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    type = forms.CharField(required=False)
    business_partner = forms.ModelChoiceField(queryset=BusinessPartner.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(AgentInfoChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs['autocomplete'] = 'off'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(

            Fieldset(
                'Authentication Information',
                'email',
                Field('business_partner', type='hidden'),
                'is_active',
            ),
            Fieldset(
                'Personal Info',
                'first_name',
                'last_name',
                'city',
                'mobile_number',
                Field('address', rows=3)
            ),

            Fieldset(
                'Mobile Information',
                'mobile_os',
                'make',
                'model'
            ),
            HTML("<br/>"),
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="{% url \'agent-list\' %}" class="btn"/>Cancel</a>'),
                css_class='center-block form-center'
            )
        )

    class Meta:
        model = AgentInfo
        exclude = ('username', 'password', 'date_joined', 'last_login', 'password1', 'password2')


