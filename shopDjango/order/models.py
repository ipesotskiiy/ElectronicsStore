from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import DecimalValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from mainapp.models import Profile
from product.models import Product, ProductType
from shopDjango.settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _


class BasketItems(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    basket = models.ForeignKey('Basket', verbose_name='Basket', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(_('Quantity product'), default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=_('Total price'))

    def __str__(self):
        return f'{self.content_object.name}'

    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.content_object.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Basket item')
        verbose_name_plural = _('Basket items')


class Basket(models.Model):
    items = models.ManyToManyField(BasketItems, related_name='related_basket', blank=True)
    owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    total_product = models.PositiveIntegerField(_('Total products'), default=0)
    final_price = models.DecimalField(_("Final price"), default=0, max_digits=9, decimal_places=2)
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, _('New order')),
        (STATUS_IN_PROGRESS, _('Order in processing')),
        (STATUS_READY, _('Order is ready')),
        (STATUS_COMPLETED, _('Order completed'))
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, _('Pickup')),
        (BUYING_TYPE_DELIVERY, _('Delivery'))
    )

    profile = models.ForeignKey(Profile, verbose_name=_('Profile'), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name=_("Buyer's name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Buyer's last name"))
    phone = models.CharField(max_length=20, verbose_name=_("Buyer's phone number"))
    basket = models.ForeignKey(Basket, verbose_name=_('Basket'), on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name=_("buyer's address"), null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name=_('Order status'),
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name=_('Order type'),
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name=_('Comment to the order'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name=_('Order creation date'))
    order_date = models.DateField(verbose_name=_('Date of receipt of the order'), default=timezone.now)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.id)
