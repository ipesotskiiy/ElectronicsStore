# Register your models here.
"""Integrate with admin module."""

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import path

from django.views.generic import DetailView

from mainapp.forms import CorgiCoin
from mainapp.models import User, Profile, AccumulativeDiscount, Wallet
from mainapp.views import AdminCorgiCoinView


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Define admin model for custom User model with no email field."""

    list_display = ('first_name', 'last_name', 'email', 'birth_day', 'age')
    list_display_links = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    change_form_template = 'admin/mainapp/custom_change_form.html'
    list_display = ('user', 'house', 'street', 'city', 'region', 'country', 'phone_number', 'static_avatar',
                    'second_name', 'full_name', 'corgi_coin',)
    list_display_links = ('user',)
    fields = ('static_avatar', 'house', 'street', 'city', 'region', 'country', 'phone_number', 'second_name', 'user',
              'corgi_coin')
    readonly_fields = ('corgi_coin',)
    search_fields = ['city__startswith', 'region__startswith', 'country__startswith', 'second_name__startswith',
                     'house__startswith']
    ordering = ('user',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<path:object_id>/corgi_coin', self.admin_site.admin_view(AdminCorgiCoinView.as_view()),
                 name='corgi_coin')
        ]
        return my_urls + urls


@admin.register(AccumulativeDiscount)
class AccumulativeDiscount(admin.ModelAdmin):
    list_display = ('discount', 'user')


@admin.register(Wallet)
class Wallet(admin.ModelAdmin):
    list_display = ('user', 'balance')




#### модель транзакции, которая хранит информацию о всех операциях пользователя (поля: пользователь, описание, время и
# сумма)

# в кошельке должны быть методы
# 1.пополнение счёта - должен создавать транзакцию (скок денег, описание, должно поменяться количество денег)
# 2.списание счёта тоже самое(создать транзакцию, списать деньги)
