from django.core.validators import DecimalValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from product.managers import ManufacturerNameQuerySet, ManufacturerNameProductManager


class ProductType(models.Model):
    type = models.CharField(_('Product type'), max_length=255)

    class Meta:
        verbose_name = _('Product type')
        verbose_name_plural = _('Product types')

    def __str__(self):
        return self.type


class Product(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(_('Product name'), db_index=True, max_length=255)
    price = models.DecimalField(_('Price'), max_digits=12, decimal_places=2, db_index=True, validators=[
        DecimalValidator(
            max_digits=11,
            decimal_places=2
        )
    ])
    manufacturer_name = models.CharField(_('manufacturer name'), db_index=True, max_length=255)
    discount = models.FloatField(blank=True, null=True, db_index=True)
    photo = models.ImageField(_('Product photo'))
    description = models.TextField(_('Description'), max_length=255)

    objects = ManufacturerNameQuerySet.as_manager()
    select_manufacturer_name = ManufacturerNameProductManager()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        unique_together = ('name', 'description')

    def __str__(self):
        return self.name


class GeneralSpecifications(models.Model):
    screen_refresh_rate_hertz = models.PositiveIntegerField(_('Screen refresh rate hertz'), db_index=True)
    screen_size = models.FloatField(_('Screen size'), db_index=True)
    screen_resolution = models.CharField(_('Screen resolution'), max_length=255, db_index=True)
    screen_matrix = models.CharField(_('Screen matrix'), max_length=255, db_index=True)
    CPU = models.CharField(_('CPU'), max_length=255, db_index=True)
    ram_in_gigabytes = models.IntegerField(_('RAM in gigabytes'), db_index=True, validators=[
        MaxValueValidator(
            limit_value=256,
            message=_('No more than two hundred and fifty six')
        ),
        MinValueValidator(
            limit_value=1,
            message=_('At least one')
        )
    ])
    Weight = models.FloatField(_("Weight in kilograms"))
    operating_system = models.CharField(_('Operating system'), db_index=True, max_length=255)
    battery_capacity_in_milliamps = models.IntegerField(_('battery capacity in milliamps'))
    built_in_memory_in_gigabytes = models.IntegerField(_('Built-in memory in gigabytes'))
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, db_index=True, validators=[
        DecimalValidator(
            max_digits=10,
            decimal_places=2
        )
    ])

    class Meta:
        abstract = True


class MobilePhone(GeneralSpecifications):
    name = models.OneToOneField(Product, on_delete=models.CASCADE, unique=True)
    number_of_camera = models.IntegerField(_('number of camera'), validators=[
        MaxValueValidator(
            limit_value=4,
            message=_('No more than four')
        ),
        MinValueValidator(
            limit_value=1,
            message=_('At least one')
        )
    ])
    number_of_SIM_cards = models.IntegerField(_('Number of SIM cards'), validators=[
        MaxValueValidator(
            limit_value=3,
            message=_('No more than three')
        ),
        MinValueValidator(
            limit_value=1,
            message=_('At least one')
        )
    ])

    class Meta:
        verbose_name = _('MobilePhone')
        verbose_name_plural = _('MobilePhones')


class Laptop(GeneralSpecifications):
    name = models.OneToOneField(Product, on_delete=models.CASCADE, unique=True)
    number_of_ram_slots = models.IntegerField(_('Number of RAM slots'), validators=[
        MaxValueValidator(
            limit_value=3,
            message=_('No more than three')
        ),
        MinValueValidator(
            limit_value=1,
            message=_('At least one')
        )
    ])
    video_card_type = models.CharField(_('Video card type'), db_index=True, max_length=255)
    video_processor = models.CharField(_('video processor'), db_index=True, max_length=255)
    memory_storage_type = models.CharField(_('memory storage type'), max_length=255)

    class Meta:
        verbose_name = _('Laptop')
        verbose_name_plural = _('Laptops')


class Freezer(models.Model):
    name = models.OneToOneField(Product, on_delete=models.CASCADE, unique=True)
    color = models.CharField(_('Color'), max_length=255)
    total_usable_volume_in_liters = models.FloatField(_('Total usable volume in liters'), db_index=True)
    minimum_temperature_in_degrees_Celsius = models.FloatField(_('Minimum temperature in degrees Celsius'))
    noise_level_in_decibels = models.FloatField(_('Noise level in decibels'))
    total_number_of_boxes = models.IntegerField(_('Total number of boxes'))
    number_of_drawers = models.IntegerField(_('Number of drawers'))
    number_of_drawers_with_doors = models.IntegerField(_('Number of drawers with doors'))
    power_consumption_in_watts = models.FloatField(_('Power consumption in watts'))
    refrigerant = models.CharField(_('refrigerant'), max_length=255)

    class Meta:
        verbose_name = _('Freezer')
        verbose_name_plural = _('Freezers')


class RefrigeratorWithFreezer(Freezer):
    freshness_zone = models.CharField(_('freshness zone'), max_length=255)
    egg_stand = models.CharField(_('Egg stand'), max_length=255)
    bottle_rack = models.CharField(_('Bottle rack'), max_length=255)
    useful_volume_of_the_refrigerating_chamber = models.CharField(
        _('Useful volume of the refrigerating chamber in liters'),
        max_length=255)
    usable_volume_of_the_freezer = models.CharField(_('Usable volume of the freezer in liters'), max_length=255,
                                                    db_index=True)

    class Meta:
        verbose_name = _('Refrigerator with Freezer')
        verbose_name_plural = _('Refrigerators with Freezer')
