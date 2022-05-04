# Register your models here.
"""Integrate with admin module."""

from django.contrib import admin
from mainapp.models import User, Profile, AccumulativeDiscount, Wallet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Define admin model for custom User model with no email field."""

    list_display = ('first_name', 'last_name', 'email', 'birth_day', 'age')
    list_display_links = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
    'house', 'street', 'city', 'region', 'country', 'phone_number', 'static_avatar', 'second_name', 'user')

    fields = ('static_avatar', 'house', 'street', 'city', 'region', 'country', 'phone_number', 'user')


@admin.register(AccumulativeDiscount)
class AccumulativeDiscount(admin.ModelAdmin):
    list_display = ('discount', 'user')


@admin.register(Wallet)
class Wallet(admin.ModelAdmin):
    list_display = ('user', 'balance')
