from django.contrib import admin
from order.models import Order, Basket, BasketItems


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('profile',)


@admin.register(Basket)
class Basket(admin.ModelAdmin):
    list_display = ('owner', 'final_price')


@admin.register(BasketItems)
class BasketItems(admin.ModelAdmin):
    list_display = ('basket', 'quantity', 'final_price')
