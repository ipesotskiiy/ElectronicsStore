from PIL import Image
from django.contrib.contenttypes.models import ContentType
from django.core.validators import DecimalValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from product.managers import ManufacturerNameQuerySet, ManufacturerNameProductManager


class MinResolutionImageErrorException(Exception):
    pass


class MaxResolutionImageErrorException(Exception):
    pass


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_product = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_product)

        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:
    objects = LatestProductManager()


class CategoryManager(models.Manager):
    CATEGORY_NAME_COUNT_NAME = {
        'Laptop': 'laptop__count',
        'Mobile phone': 'mobilephone__count',
        'Freezer': 'freezer__count'
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_models_for_count('laptop', 'mobilephone', 'freezer')
        qs = list(self.get_queryset().annotate(*models))
        type_pr = [t.type for t in qs]
        data = [
            dict(name=c.type, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.type]))
            for c in qs
        ]
        return data


class ProductType(models.Model):
    type = models.CharField(_('Product type'), max_length=255)
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def get_absolute_url(self):
        return reverse('product:category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = _('Product type')
        verbose_name_plural = _('Product types')

    def __str__(self):
        return self.type


class Product(models.Model):
    MIN_RESOLUTION_FOR_IMAGE = (400, 400)
    MAX_RESOLUTION_FOR_IMAGE = (4000, 4000)
    MAX_IMAGE_SIZE = 3145728

    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(_('Product name'), db_index=True, max_length=255)
    price = models.DecimalField(_('Price'), max_digits=12, decimal_places=2, db_index=True, validators=[
        DecimalValidator(
            max_digits=11,
            decimal_places=2
        )
    ])
    slug = models.SlugField(unique=True)
    manufacturer_name = models.CharField(_('Manufacturer name'), db_index=True, max_length=255)
    discount = models.FloatField(_('Discount'), blank=True, null=True, db_index=True)
    photo = models.ImageField(_('Product photo'))
    description = models.TextField(_('Description'), max_length=255)
    objects = ManufacturerNameQuerySet.as_manager()
    select_manufacturer_name = ManufacturerNameProductManager()
    color = models.CharField(_('Color'), max_length=255)
    count = models.PositiveIntegerField(_('Quantity in stock'))

    def get_model_name(self):
        return self.__class__.__name__.lower()

    def save(self, *args, **kwargs):
        image = self.photo
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION_FOR_IMAGE
        max_height, max_width = self.MAX_RESOLUTION_FOR_IMAGE

        if img.height < min_height or img.width < min_width:
            raise MinResolutionImageErrorException(
                _('Image resolution is less than minimum!'
                  'Your image size {}x{} minimum resolution {}x{}').format(img.height, img.width,
                                                                           min_height, min_width))
        if img.height > max_height or img.width > max_width:
            raise MaxResolutionImageErrorException(
                _('Image resolution is less than minimum!'
                  'Your image size {}x{} minimum resolution {}x{}').format(img.height, img.width,
                                                                           min_height, min_width))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MobilePhone(Product):
    number_of_camera = models.IntegerField(_('Number of camera'), validators=[
        MaxValueValidator(
            limit_value=4,
            message=_('No more than four')
        ),
        MinValueValidator(
            limit_value=1,
            message=_('At least one')
        )
    ])
    number_of_sim_cards = models.IntegerField(_('Number of SIM cards'), validators=[
        MaxValueValidator(
            limit_value=3,
            message=_('No more than three')
        ),
        MinValueValidator(
            limit_value=1,
            message=_('At least one')
        )
    ])
    screen_refresh_rate_hertz = models.PositiveIntegerField(_('Screen refresh rate hertz'), db_index=True)
    screen_size = models.FloatField(_('Screen size'), db_index=True)
    screen_resolution = models.CharField(_('Screen resolution'), max_length=255, db_index=True)
    screen_matrix = models.CharField(_('Screen matrix'), max_length=255, db_index=True)
    cpu_name = models.CharField(_('CPU'), max_length=255, db_index=True)
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
    weight = models.FloatField(_("Weight in kilograms"))
    operating_system = models.CharField(_('Operating system'), db_index=True, max_length=255)
    battery_capacity_in_milliamps = models.IntegerField(_('Battery capacity in milliamps'))
    built_in_memory_in_gigabytes = models.IntegerField(_('Built-in memory in gigabytes'))

    def get_absolute_url(self):
        return get_product_url(self, 'product:product_detail')

    class Meta:
        verbose_name = _('Mobile Phone')
        verbose_name_plural = _('Mobile Phones')

    def __str__(self):
        return str(self.type)


class Laptop(Product):
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
    video_processor = models.CharField(_('Video processor'), db_index=True, max_length=255)
    memory_storage_type = models.CharField(_('Memory storage type'), max_length=255)
    screen_refresh_rate_hertz = models.PositiveIntegerField(_('Screen refresh rate hertz'), db_index=True)
    screen_size = models.FloatField(_('Screen size'), db_index=True)
    screen_resolution = models.CharField(_('Screen resolution'), max_length=255, db_index=True)
    screen_matrix = models.CharField(_('Screen matrix'), max_length=255, db_index=True)
    cpu_name = models.CharField(_('CPU'), max_length=255, db_index=True)
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
    weight = models.FloatField(_("Weight in kilograms"))
    operating_system = models.CharField(_('Operating system'), db_index=True, max_length=255)
    battery_capacity_in_milliamps = models.IntegerField(_('Battery capacity in milliamps'))
    built_in_memory_in_gigabytes = models.IntegerField(_('Built-in memory in gigabytes'))

    def get_absolute_url(self):
        return get_product_url(self, 'product:product_detail')

    class Meta:
        verbose_name = _('Laptop')
        verbose_name_plural = _('Laptops')

    def __str__(self):
        return str(self.name)


class Freezer(Product):
    total_usable_volume_in_liters = models.FloatField(_('Total usable volume in liters'), db_index=True)
    minimum_temperature_in_degrees_Celsius = models.FloatField(_('Minimum temperature in degrees Celsius'))
    noise_level_in_decibels = models.FloatField(_('Noise level in decibels'))
    total_number_of_boxes = models.IntegerField(_('Total number of boxes'))
    number_of_drawers = models.IntegerField(_('Number of drawers'))
    number_of_drawers_with_doors = models.IntegerField(_('Number of drawers with doors'))
    power_consumption_in_watts = models.FloatField(_('Power consumption in watts'))
    refrigerant = models.CharField(_('Refrigerant'), max_length=255)

    def get_absolute_url(self):
        return get_product_url(self, 'product:product_detail')

    class Meta:
        verbose_name = _('Freezer')
        verbose_name_plural = _('Freezers')

    def __str__(self):
        return str(self.name)
