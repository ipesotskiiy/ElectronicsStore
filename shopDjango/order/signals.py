from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

import order


@receiver(post_save, sender=order.models.Order)
def post_save_type(created, **kwargs):
    instance = kwargs['instance']
    if created:
        print(f'Заказ {instance.user} успешно создан')
    else:
        print(f'Заказ {instance.user} успешно обновлён')


@receiver(post_delete, sender=order.models.Order)
def post_delete_type(**kwargs):
    instance = kwargs['instance']
    print(f'Заказ {instance.user} успешно удалён')
