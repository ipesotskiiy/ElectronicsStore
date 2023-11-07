from django.views.generic import DetailView

from order.mixins import BasketMixin
from product.mixins import CategoryDetailMixin
from product.models import Laptop, MobilePhone, Freezer, ProductType


class ProductDetailView(BasketMixin, CategoryDetailMixin, DetailView):
    CT_MODEL_MODEL_CLASS = {
        'laptop': Laptop,
        'mobilephone': MobilePhone,
        'freezer': Freezer
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product/product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        context['basket'] = self.basket
        return context


class CategoryDetailView(BasketMixin, CategoryDetailMixin, DetailView):

    model = ProductType
    queryset = ProductType.objects.all()
    context_object_name = 'type'
    template_name = 'product/category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = self.basket
        return context

