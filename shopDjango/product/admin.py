from django.contrib import admin
from product.models import Product, ProductType, MobilePhone, Laptop, Freezer, RefrigeratorWithFreezer


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('type', 'name', 'manufacturer_name', 'discount', 'photo', 'price')


@admin.register(ProductType)
class ProductType(admin.ModelAdmin):
    list_display = ('type',)


@admin.register(MobilePhone)
class MobilePhone(admin.ModelAdmin):
    list_display = [f.name for f in MobilePhone._meta.get_fields()]


@admin.register(Laptop)
class Laptop(admin.ModelAdmin):
    list_display = [f.name for f in Laptop._meta.get_fields()]


@admin.register(Freezer)
class Freezer(admin.ModelAdmin):
    list_display = [f.name for f in Freezer._meta.get_fields()]


@admin.register(RefrigeratorWithFreezer)
class RefrigeratorWithFreezer(admin.ModelAdmin):
    list_display = [f.name for f in RefrigeratorWithFreezer._meta.get_fields()]
