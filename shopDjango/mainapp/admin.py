from django.contrib import admin

# Register your models here.
"""Integrate with admin module."""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Define admin model for custom User model with no email field."""

    list_display = ('first_name', 'last_name', 'second_name', 'email', 'birth_day')