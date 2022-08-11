from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext_lazy as _

from order.forms import OrderForm
from order.mixins import BasketMixin
from mainapp.models import Profile
from order.models import Basket, BasketItems
from order.utils import recalc_basket
from product.models import ProductType


class BasketView(BasketMixin, View):

    def get(self, request, *args, **kwargs):
        types = ProductType.objects.get_categories_for_left_sidebar()
        context = {
            'basket': self.basket,
            'types': types
        }
        return render(request, 'order_and_basket/basket.html', context)


class CheckoutView(BasketMixin, View):

    def get(self, request, *args, **kwargs):
        types = ProductType.objects.get_categories_for_left_sidebar()
        form = OrderForm(request.POST or None)
        context = {
            'basket': self.basket,
            'types': types,
            'form': form
        }
        return render(request, 'order_and_basket/checkout.html', context)


class AddToBasketView(BasketMixin, View):

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        basket_product, created = BasketItems.objects.get_or_create(
            user=request.user.profile, basket=self.basket, content_type=content_type, object_id=product.id
        )
        if created:
            self.basket.items.add(basket_product)
        recalc_basket(self.basket)
        messages.add_message(request, messages.INFO, _("Product added successfully"))
        return HttpResponseRedirect('/orders/basket/')


class DeleteFromCartView(BasketMixin, View):

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        basket_product = BasketItems.objects.get(
            user=request.user.profile, basket=self.basket, content_type=content_type, object_id=product.id
        )
        self.basket.items.remove(basket_product)
        basket_product.delete()
        recalc_basket(self.basket)
        messages.add_message(request, messages.INFO, _("Product deleted successfully"))
        return HttpResponseRedirect('/orders/basket/')


class ChangeQTYView(BasketMixin, View):

    def post(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        basket_product = BasketItems.objects.get(
            user=request.user.profile, basket=self.basket, content_type=content_type, object_id=product.id
        )
        quantity = int(request.POST.get('qty'))
        basket_product.quantity = quantity
        basket_product.save()
        recalc_basket(self.basket)
        messages.add_message(request, messages.INFO, _("Quantity changed successfully"))
        return HttpResponseRedirect('/orders/basket/')


class MakeOrderView(BasketMixin, View):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        profile = Profile.objects.get(user=request.user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.profile = profile
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.order_date = form.cleaned_data['order_date']
            new_order.comment = form.cleaned_data['comment']
            new_order.save()
            self.basket.in_order = True
            self.basket.save()
            new_order.basket = self.basket
            new_order.save()
            profile.orders.add(new_order)
            messages.add_message(request, messages.INFO, _('Thanks for your order! The manager will contact you.'))
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/checkout/')
