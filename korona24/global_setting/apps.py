from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GlobalSettingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'global_setting'
    verbose_name = _('Настройки сайта')
