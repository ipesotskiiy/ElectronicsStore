from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from mainapp import models
from mainapp.models import Profile
from shopDjango import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def link_to_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
