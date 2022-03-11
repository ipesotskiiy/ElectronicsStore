from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

import mainapp.models
from shopDjango import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_user(created, instance, **kwargs):
    if created:
        print(f'Пользователь {instance.email} успешно создан')
    else:
        print(f'Пользователь {instance.email} успешно обновлён')


@receiver(post_delete, sender=settings.AUTH_USER_MODEL)
def post_delete_type(instance, **kwargs):
    print(f'Пользователь {instance.email} успешно удалён')


@receiver(post_save, sender=mainapp.models.Profile)
def post_save_profile(created, instance, **kwargs):
    if created:
        print('Профиль успешно создан')
    else:
        print('Профиль успешно обновлён')


@receiver(post_delete, sender=mainapp.models.Profile)
def post_delete_type(instance, **kwargs):
    print(f'Профиль успешно удалён')
