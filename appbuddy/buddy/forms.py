from crispy_forms.bootstrap import FormActions, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, ButtonHolder, HTML, Field, Fieldset, Hidden
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.forms import ModelForm
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode

from .models import DeviceInfo, Category, CityInfo, DataCardInfo, BaseUser, BusinessPartner, LocationPartner, \
    LocationInfo, AgentInfo, AppInfo, WhitelistUrl


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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
            )
        )

    class Meta:
        model = BusinessPartner
        exclude = ('username', 'password', 'date_joined', 'last_login')


class AgentInfoCreationForm(BaseUserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True, )
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
            )
        )

    class Meta:
        model = AgentInfo
        exclude = ('username', 'password', 'date_joined', 'last_login', 'agent_id')

    def save(self, commit=True):
        user = super(AgentInfoCreationForm, self).save(commit)

        return user


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
                'business_partner'
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
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
                'business_partner',
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
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
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
            )
        )

    class Meta:
        model = AgentInfo
        exclude = ('username', 'password', 'date_joined', 'last_login', 'password1', 'password2')


class AppInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs['autocomplete'] = 'off'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'package_name',
            'name',
            Field('description', rows=4),
            'market_url',
            'categories',
            'cities',
            'min_android_version',
            'active',
            'open_on_install',
            'download_time_wifi',
            'download_time_3g',
            'download_time_edge',
            'thumbnail',
            Field('proxy_whitelist', rows=3),
            Field('dns_whitelist', rows=3),
            HTML("<br/>"),
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
            )
        )

    class Meta:
        model = AppInfo


class AppBuddyPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        email = self.cleaned_data["email"]
        active_users = BaseUser._default_manager.filter(
            email__iexact=email, is_active=True)
        for user in active_users:
            # Make sure that no email is sent to a user that actually has
            # a password marked as unusable
            if not user.has_usable_password():
                continue
            if not domain_override:
                current_site = Site.objects.get_current()
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }
            subject = loader.render_to_string(subject_template_name, c)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)
            text_content = strip_tags(email)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [user.email])
            msg.attach_alternative(email, "text/html")
            msg.send()
            # send_mail(subject, email, from_email, [user.email])


class LocationAssignForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocationAssignForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            'device_info',
            'agent',
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary'),
                HTML('<a href="#" class="btn cancel"/>Cancel</a>'),
                css_class='center-block form-center text-center'
            )
        )

    class Meta:
        model = LocationInfo
        exclude = (
            'name', 'partner', 'address', 'area', 'city', 'store_manager_name', 'store_manager_number', 'foot_fall',
            'landline_number', 'preferred_days', 'preferred_time', 'latitude', 'longitude' )



