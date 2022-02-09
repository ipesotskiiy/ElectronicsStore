from django.contrib import admin

# Register your models here.
"""Integrate with admin module."""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Define admin model for custom User model with no email field."""

    list_display = ('first_name', 'last_name', 'second_name', 'email', 'birth_day', 'age')
    list_display_links = ('email',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('house', 'street', 'city', 'region', 'country', 'phone_number')
