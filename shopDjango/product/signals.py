from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

import product.models


@receiver(post_save, sender=product.models.ProductType)
def post_save_type(created, instance, **kwargs):
    if created:
        print(f'Тип {instance.type} успешно создан')
    else:
        print(f'Тип {instance.type} успешно обновлён')


@receiver(post_delete, sender=product.models.ProductType)
def post_delete_type(instance, **kwargs):
    print(f'Тип {instance.type} успешно удалён')


@receiver(post_save, sender=product.models.Product)
def post_save_product(created, instance, **kwargs):
    if created:
        print(f'Продукт {instance.name} успешно создан')
    else:
        print(f'Продукт {instance.name} успешно обновлён')


@receiver(post_delete, sender=product.models.Product)
def post_delete_product(instance, **kwargs):
    print(f'Продукт {instance.name} успешно удалён')


@receiver(post_save, sender=product.models.MobilePhone)
def post_save_mobile_phone(created, instance, **kwargs):
    if created:
        print(f'Мобильный телефон {instance.name} успешно создан')
    else:
        print(f'Мобильный телефон {instance.name} успешно обновлён')


@receiver(post_delete, sender=product.models.MobilePhone)
def post_delete_mobile_phone(instance, **kwargs):
    print(f'Мобильный телефон {instance.name} успешно удалён')


@receiver(post_save, sender=product.models.Laptop)
def post_save_laptop(created, instance, **kwargs):
    if created:
        print(f'Ноутбук {instance.name} успешно создан')
    else:
        print(f'Ноутбук {instance.name} успешно обновлён')


@receiver(post_delete, sender=product.models.Laptop)
def post_delete_laptop(instance, **kwargs):
    print(f'Ноутбук {instance.name} успешно удалён')
