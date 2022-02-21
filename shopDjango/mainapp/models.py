from django.core.validators import RegexValidator
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, User
from mainapp.managers import UserManager
from datetime import date, datetime


def get_path(instance, file_name):
    return "/".join([str(instance.name), file_name])


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

    @property
    def age(self):
        if self.birth_day:
            today = now()
            return today.year - self.birth_day.year - (
                    (today.month, today.day) < (self.birth_day.month, self.birth_day.day))
        return 0


class Profile(models.Model):
    house = models.CharField(verbose_name='House', max_length=255, blank=True)
    street = models.CharField(verbose_name='Street', max_length=255, blank=True)
    city = models.CharField(verbose_name='City', max_length=255, blank=True)
    region = models.CharField(verbose_name='Region', max_length=255, blank=True)
    country = models.CharField(verbose_name="Country", max_length=255, blank=True)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}',
                                 message="Phone number must be entered in the format: '+999999999'")
    phone_number = models.CharField(verbose_name='Phone', max_length=12, blank=True, validators=[phone_regex])
    static_avatar = models.ImageField(verbose_name='Avatar', upload_to=get_path, null=True,
                                      blank=True)