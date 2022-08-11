from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login
from django.views.generic import DetailView

from mainapp.forms import RegistrationUser, CorgiCoin, ProfileForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from mainapp.models import User, Profile
from order.mixins import BasketMixin
from product.models import ProductType, LatestProducts

menu = ['Войти', 'Регистрация', "Профиль"]
product_list = ProductType.objects.all


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


class AdminCorgiCoinView(PermissionRequiredMixin, View):
    permission_required = ["change_profile"]

    def get(self, request, object_id):
        tempate_name = 'admin/mainapp/corgi_coin.html'
        form_class = CorgiCoin
        return render(request, tempate_name, {'form': form_class, 'title': 'Corgi coin'})

    def post(self, request, object_id):
        tempate_name = 'admin/mainapp/corgi_coin.html'
        form_class = CorgiCoin(request.POST)
        if form_class.is_valid():
            profile = Profile.objects.get(id=object_id)
            corgi = form_class.cleaned_data.get('corgi_coin')
            profile.corgi_coin += corgi
            profile.save()
            return redirect('../')


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        dict_current_value_profile = {'house': request.user.profile.house,
                                      'street': request.user.profile.street,
                                      'city': request.user.profile.city,
                                      'region': request.user.profile.region,
                                      'country': request.user.profile.country,
                                      'phone_number': request.user.profile.phone_number,
                                      'static_avatar': request.user.profile.static_avatar,
                                      'second_name': request.user.profile.second_name}
        template_name = 'mainapp/profile_page.html'
        form_class = ProfileForm(initial=dict_current_value_profile)
        return render(request, template_name, {'form': form_class, 'title': 'Profile page',
                                               'avatar': request.user.profile.static_avatar.url})

    def post(self, request, *args, **kwargs):
        template_name = 'mainapp/profile_page.html'
        profile = request.user.profile
        form_class = ProfileForm(request.POST, request.FILES, instance=profile)
        if form_class.is_valid():
            # image = request.FILES.get('static_avatar')
            profile = form_class.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('user:profile_page')
        else:
            form_class = ProfileForm()
            return redirect('home')


class BaseView(BasketMixin,View):
    def get(self, request, *args, **kwargs):
        categories = ProductType.objects.get_categories_for_left_sidebar()
        products = LatestProducts.objects.get_products_for_main_page(
            'laptop', 'mobilephone', 'freezer', with_respect_to='laptop'
        )
        context = {
            'categories': categories,
            'products': products,
            'basket': self.basket
        }
        return render(request, 'mainapp/base.html', context)
