from django.views.generic.detail import SingleObjectMixin

from product.models import Laptop, MobilePhone, Freezer, ProductType


class CategoryDetailMixin(SingleObjectMixin):
    CATEGORY_SLUG3PRODUCT_MODEL = {
        'laptop': Laptop,
        'mobile_phone': MobilePhone,
        'freezer': Freezer
    }

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), ProductType):
            model = self.CATEGORY_SLUG3PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['type'] = ProductType.objects.get_categories_for_left_sidebar()
            context['category_products'] = model.objects.all()
            return context
        context = super().get_context_data(**kwargs)
        context['type'] = ProductType.objects.get_categories_for_left_sidebar()
        return context
