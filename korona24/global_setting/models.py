from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
 


class SiteSetting(models.Model):
    """
    Модель настроек сайта.
    Модель наследует поведение SingletonModel, реализующей паттен Singleton.
    Модель может иметь только один экземпляр и одну запись в БД.
    """

    years_on_market = models.IntegerField(
        validators=[validators.MinValueValidator(0)],
        null=True,
        blank=True,
        verbose_name=_('Лет на рынке'),
    )
    count_operations = models.IntegerField(
        validators=[validators.MinValueValidator(0)],
        null=True,
        blank=True,
        verbose_name=_('Кол-во операций под общим наркозом'),
    )
    count_doctors = models.IntegerField(
        validators=[validators.MinValueValidator(0)],
        null=True,
        blank=True,
        verbose_name=_('Кол-во профессиональных врачей'),
    )
    count_patients = models.IntegerField(
        validators=[validators.MinValueValidator(0)],
        null=True,
        blank=True,
        verbose_name=_('Кол-во пацинатов в год'),
    )
    enabled_partners = models.BooleanField(
        default=False,
        verbose_name=_('Отображать партнеров'),
        help_text=_('Включает или отключает блок партнеров на сайте.'),
    )

    code_in_html = models.TextField(
        verbose_name=_('Добавить скрипты в HEAD'),
        help_text=_('Сюда можно вставить код Яндекс метрики и Google Analytics'),
        null=True,
        blank=True
    )
    
    class Meta:
        """Настройки модели"""
        verbose_name = _('Настройки сайта')
        verbose_name_plural = _('Настройки сайта')

    def __str__(self) -> str:
        return str(self.__class__._meta.verbose_name)


class PhoneAndAddres(models.Model):
    """Модель для хранения телефонов и адресов"""

    address = models.TextField(
        verbose_name=_('Адрес'),
    )
    phone_number = models.TextField( 
        verbose_name=_('Номер телефона'),
    )
    site_settings = models.ForeignKey(
        to=SiteSetting,
        on_delete=models.CASCADE,
        related_name='phone_and_address_set',
        related_query_name='phone_and_address',
    )

    class Meta:
        """Настройки модели"""
        verbose_name = _('Телефон и адрес')
        verbose_name_plural = _('Телефоны и адреса')

    def __str__(self) -> str:
        return str(self.address)