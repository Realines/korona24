from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators


class Discount(models.Model):
    title = models.TextField( 
        verbose_name=_('Заголовок'),
    )
    description = models.TextField( 
        verbose_name=_('Описание'),
    )

    date_added = models.DateField(
        verbose_name=_('Дата заявки'),
        auto_now_add=True,
    )
    show_on_main = models.BooleanField(
        verbose_name=_('Показать на главной'),
        default=False,
    )
    class Meta:
        verbose_name = _('Акции на главной')
        verbose_name_plural = _('Акции на главной')
        ordering = ['-date_added']
        get_latest_by = 'date_added'

    def __str__(self) -> str:
        return f'{self.client_name}#{self.pk}'

class Consultation(models.Model):
    client_name = models.CharField(
        max_length=128,
        verbose_name=_('Имя клиента'),
    )
    phone_number = models.CharField(  # TODO: Найти хороший способ валидации номеров.
        max_length=16,
        verbose_name=_('Номер телефона'),
    )
    date_added = models.DateField(
        verbose_name=_('Дата заявки'),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('Консультация')
        verbose_name_plural = _('Консультации')
        ordering = ['-date_added']
        get_latest_by = 'date_added'

    def __str__(self) -> str:
        return f'{self.client_name}#{self.pk}'
