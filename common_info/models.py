from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators

from utils.models.singleton_model import SingletonModel


class SiteSettings(SingletonModel):
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

    class Meta:
        """Настройки модели"""
        verbose_name = _('Настройки сайта')
        verbose_name_plural = _('Настройки сайта')

    def __str__(self) -> str:
        return str(self.__class__._meta.verbose_name)


class SocialNetwork(models.Model):
    """
    Модель социальной сети для общих настроек сайта.
    Используется со связью многие к одному (многие соц.
    сети к одной настройке сайта).
    """

    icon = models.ImageField(
        upload_to='sys/social_networks_icons',
        verbose_name=_('Иконка социальной сети'),
    )
    name = models.TextField(
        verbose_name=_('Название соц. сети'),
    )
    url = models.URLField(
        verbose_name=_('Ссылка на соц. сеть'),
    )
    site_settings = models.ForeignKey(
        to=SiteSettings,
        on_delete=models.CASCADE,
        related_name='social_networks',
        related_query_name='social_network',
    )

    class Meta:
        """Настройки модели"""
        verbose_name = _('Социальная сеть')
        verbose_name_plural = _('Социальные сети')

    def __str__(self) -> str:
        return str(self.name)


class PhoneAndAddress(models.Model):
    """Модель для хранения телефонов и адресов"""

    address = models.TextField(
        verbose_name=_('Адрес'),
    )
    phone_number = models.TextField(  # TODO: Реализовать валидацию номера телефона.
        verbose_name=_('Номер телефона'),
    )
    site_settings = models.ForeignKey(
        to=SiteSettings,
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
