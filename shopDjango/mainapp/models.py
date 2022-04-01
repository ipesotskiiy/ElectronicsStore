from django.core.validators import RegexValidator, DecimalValidator, EmailValidator
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from mainapp.managers import UserManager


def get_path(instance, file_name):
    return "/".join([str(instance.name), file_name])


class User(AbstractUser):
    """User model"""

    objects = UserManager()

    username = None
    email = models.EmailField(_('email address'), unique=True, db_index=True, validators=[
        EmailValidator(
            message=_('Please enter a valid email address with the following domains: yandex, rambler, gmail, mail'),
            allowlist=['localhost', 'ynd', 'yandex', 'rambler', 'gmail', 'mail']
        )
    ])

    second_name = models.CharField(_('Second name'), max_length=255, blank=True)
    birth_day = models.DateField(_('Birth day'), max_length=255, db_index=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def age(self):
        if self.birth_day:
            today = now()
            return today.year - self.birth_day.year - (
                    (today.month, today.day) < (self.birth_day.month, self.birth_day.day))
        return 0

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Profile(models.Model):
    house = models.CharField(_('House'), max_length=255, blank=True)
    street = models.CharField(_('Street'), max_length=255, blank=True)
    city = models.CharField(_('City'), max_length=255, db_index=True, blank=True)
    region = models.CharField(_('Region'), max_length=255, db_index=True, blank=True)
    country = models.CharField(_('Country'), max_length=255, db_index=True, blank=True)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}',
                                 message=_("Phone number must be entered in the format: '+999999999'"))
    phone_number = models.CharField(_('Phone'), max_length=12, blank=True, validators=[phone_regex])
    static_avatar = models.ImageField(_('Avatar'), upload_to=get_path, null=True,
                                      blank=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class AccumulativeDiscount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discount = models.FloatField(_('Discount'), db_index=True)

    class Meta:
        verbose_name = _('Accumulative discount')
        verbose_name_plural = _('Accumulative discounts')


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(_('Balance'), max_digits=12, decimal_places=2, validators=[
        DecimalValidator(
            max_digits=11,
            decimal_places=2
        )
    ])

    class Meta:
        permissions = (('Can_add_money', 'Top add balance'),)
        verbose_name = _('Wallet')
        verbose_name_plural = _('Wallets')
