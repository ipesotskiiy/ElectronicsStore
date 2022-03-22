# Register your models here.
"""Integrate with admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, AccumulativeDiscount, Wallet


# admin.site.register(User, UserAdmin)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Define admin model for custom User model with no email field."""

    list_display = ('first_name', 'last_name', 'second_name', 'email', 'birth_day', 'age')
    list_display_links = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('house', 'street', 'city', 'region', 'country', 'phone_number', 'static_avatar')

    fields = ('static_avatar',)
    readonly_fields = ('static_avatar',)


@admin.register(AccumulativeDiscount)
class AccumulativeDiscount(admin.ModelAdmin):
    list_display = ('discount', 'user')


@admin.register(Wallet)
class Wallet(admin.ModelAdmin):
    list_display = ('user', 'balance')
