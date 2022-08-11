from django.forms import ModelChoiceField
from django.contrib import admin
from product.forms import ImageAdminForm
from product.models import ProductType as ProductTypeModel, MobilePhone, Laptop, Freezer


@admin.register(ProductTypeModel)
class ProductType(admin.ModelAdmin):
    list_display = ('type',)


@admin.register(MobilePhone)
class MobilePhone(admin.ModelAdmin):
    form = ImageAdminForm
    list_display = [f.name for f in MobilePhone._meta.get_fields()]
    list_filter = ('price',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type':
            return ModelChoiceField(ProductTypeModel.objects.filter(slug='mobile_phone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Laptop)
class Laptop(admin.ModelAdmin):
    form = ImageAdminForm
    list_display = [f.name for f in Laptop._meta.get_fields()]
    list_filter = ('price',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type':
            return ModelChoiceField(ProductTypeModel.objects.filter(slug='laptop'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Freezer)
class Freezer(admin.ModelAdmin):
    form = ImageAdminForm
    list_display = [f.name for f in Freezer._meta.get_fields()]
    list_filter = ('price',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type':
            return ModelChoiceField(ProductTypeModel.objects.filter(slug='freezer'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
