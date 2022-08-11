from django.db import models


class ManufacturerNameQuerySet(models.QuerySet):
    def apple(self):
        return self.filter(manufacturer_name='Apple')

    def acer(self):
        return self.filter(manufacturer_name='Acer')


class ManufacturerNameProductManager(models.Manager):
    def apple(self):
        return self.get_queryset().apple()

    def acer(self):
        return self.get_queryset().acer()


