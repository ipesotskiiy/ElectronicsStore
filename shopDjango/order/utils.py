from django.db import models


def recalc_basket(basket):
    basket_data = basket.items.aggregate(models.Sum('final_price'), models.Count('id'))
    if basket_data.get('final_price__sum'):
        basket.final_price = basket_data['final_price__sum']
    else:
        basket.final_price = 0
    basket.total_product = basket_data['id__count']
    basket.save()