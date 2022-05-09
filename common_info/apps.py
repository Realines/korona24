from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common_info'
    verbose_name = _('Настройки сайта')
