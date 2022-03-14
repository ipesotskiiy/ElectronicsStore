from django.db import models
from django.utils.translation import gettext_lazy as _

from product.managers import ManufacturerNameQuerySet, ManufacturerNameProductManager


class ProductType(models.Model):
    type = models.CharField(_('Product type'), max_length=255)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = _('Product type')
        verbose_name_plural = _('Product types')


class Product(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(_('Product name'), max_length=255)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)
    manufacturer_name = models.CharField(_('manufacturer name'), max_length=255)
    discount = models.FloatField(blank=True, null=True)
    photo = models.ImageField(_('Product photo'))

    objects = ManufacturerNameQuerySet.as_manager()
    select_manufacturer_name = ManufacturerNameProductManager()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class GeneralSpecifications(models.Model):
    screen_refresh_rate_hertz = models.PositiveIntegerField(_('Screen refresh rate hertz'))
    screen_size = models.FloatField(_('Screen size'))
    screen_resolution = models.CharField(_('Screen resolution'), max_length=255)
    screen_matrix = models.CharField(_('Screen matrix'), max_length=255)
    CPU = models.CharField(_('CPU'), max_length=255)
    ram_in_gigabytes = models.IntegerField(_('RAM in gigabytes'))
    Weight = models.FloatField(_("Weight in kilograms"))
    operating_system = models.CharField(_('Operating system'), max_length=255)
    battery_capacity_in_milliamps = models.IntegerField(_('battery capacity in milliamps'))
    built_in_memory_in_gigabytes = models.IntegerField(_('Built-in memory in gigabytes'))
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)

    class Meta:
        abstract = True


class MobilePhone(GeneralSpecifications):
    name = models.OneToOneField(Product, on_delete=models.CASCADE)
    number_of_camera = models.IntegerField(_('number of camera'))
    number_of_SIM_cards = models.IntegerField(_('Number of SIM cards'))

    class Meta:
        verbose_name = _('MobilePhone')
        verbose_name_plural = _('MobilePhones')


class Laptop(GeneralSpecifications):
    name = models.OneToOneField(Product, on_delete=models.CASCADE)
    number_of_ram_slots = models.IntegerField(_('Number of RAM slots'))
    video_card_type = models.CharField(_('Video card type'), max_length=255)
    video_processor = models.CharField(_('video processor'), max_length=255)
    memory_storage_type = models.CharField(_('memory storage type'), max_length=255)

    class Meta:
        verbose_name = _('Laptop')
        verbose_name_plural = _('Laptops')
