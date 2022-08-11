from django.urls import path

from order.views import *

app_name = 'orders'

urlpatterns = [
    path('basket/', BasketView.as_view(), name='basket'),
    path('add-to-basket/<str:ct_model>/<str:slug>/', AddToBasketView.as_view(), name='add_to_basket'),
    path('remove-from-basket/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='remove_from_basket'),
    path('change-quantity/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change-quantity'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order')
]