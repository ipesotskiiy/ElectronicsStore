from django.contrib import admin
from order.models import Order, OrderItems, Basket, BasketItems


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('user', 'total_price')


@admin.register(OrderItems)
class OrderItems(admin.ModelAdmin):
    list_display = ('order', 'product')


@admin.register(Basket)
class Basket(admin.ModelAdmin):
    list_display = ('user', 'total_price')


@admin.register(BasketItems)
class BasketItems(admin.ModelAdmin):
    list_display = ('basket', 'product', 'quantity')
