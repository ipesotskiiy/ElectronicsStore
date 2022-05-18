from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator as token_generator

from mainapp.models import User, Profile


class RegistrationUser(UserCreationForm):
    email = forms.EmailField(label=_('email'), widget=forms.EmailInput)
    birth_day = forms.DateField(label=_('Birth day'), widget=forms.DateInput(
        attrs={'placeholder': 'Birth Date', 'class': 'form-control', 'type': 'date', }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))

    @staticmethod
    def email_message(request, user):
        current_site = get_current_site(request)
        context = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': token_generator.make_token(user)
        }

        message = render_to_string(
            'registration/verify_email.html',
            context=context
        )

        email = EmailMessage(
            'Verify email',
            message,
            to=[user.email]
        )

        email.send()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birth_day', 'password1', 'password2')


class CorgiCoin(forms.ModelForm):
    corgi_coin = forms.IntegerField(label=_('Corgi coin'), widget=forms.NumberInput)

    class Meta:
        model = Profile
        fields = ('corgi_coin',)

