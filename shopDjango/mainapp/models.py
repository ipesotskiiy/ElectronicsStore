from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from mainapp.managers import UserManager


class User(AbstractUser):
    """User model"""
    # сделать подпись добавить метаданные
    objects = UserManager()

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    second_name = models.CharField(verbose_name="Second name", max_length=255, blank=True)
    birth_day = models.DateField(verbose_name='Birth day', max_length=255, null=True)


class Profile(models.Model):
    house = models.CharField(verbose_name='House', max_length=255, blank=True)
    street = models.CharField(verbose_name='Street', max_length=255, blank=True)
    city = models.CharField(verbose_name='City', max_length=255, blank=True)
    region = models.CharField(verbose_name='Region', max_length=255, blank=True)
    country = models.CharField(verbose_name="Country", max_length=255, blank=True)

