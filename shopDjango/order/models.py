from django.db import models
from product.models import Product
from shopDjango.settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(_("Total price"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.total_price)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  related_name="content_%(class)s")

    class Meta:
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')


class Basket(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(_("Total price"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')

    def __str__(self):
        return str(self.total_price)


class BasketItems(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_('Quantity product'), default=1)

    class Meta:
        verbose_name = _('Basket item')
        verbose_name_plural = _('Basket items')
