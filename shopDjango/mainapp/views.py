from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from mainapp.forms import RegistrationUser
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from mainapp.models import User


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('user:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, ValidationError):
            user = None
        return user


class Registration(View):

    def get(self, request, *args, **kwargs):
        form_class = RegistrationUser
        template_name = 'registration/registration.html'
        return render(request, template_name, {'form': form_class, 'title': 'Registration'})

    def post(self, request, *args, **kwargs):
        template_name = 'registration/registration.html'
        form = RegistrationUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            form.email_message(request, user)
            return redirect('user:confirm_email')

        else:
            form = RegistrationUser()
            return render(request, template_name, {'form': form, 'title': 'Registration'})


class BaseView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "mainapp/base.html", {})
