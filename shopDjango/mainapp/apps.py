from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'
    verbose_name = _('User information')

    def ready(self):
        import mainapp.signals
