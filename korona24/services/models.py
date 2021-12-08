from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators

from markdown import markdown
from blog.models import Article


class Service(models.Model):
    name = models.TextField(
        verbose_name=_('Название услуги'),
    )
    description = models.TextField(
        verbose_name=_('Описание услуги'),
    )
    blog_articles = models.ManyToManyField(
        to=Article,
        verbose_name=_('Статьи блога'),
        related_name='services',
        related_query_name='service',
    )

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def __str__(self) -> str:
        return str(self.name)


class Therapy(models.Model):
    name = models.TextField(
        verbose_name=_('Название'),
    )
    price = models.IntegerField(
        verbose_name=_('Цена'),
        validators=[validators.MinValueValidator(0)],
    )
    service = models.ForeignKey(
        to=Service,
        on_delete=models.CASCADE,
        related_name='therapies',
        related_query_name='therapy',
    )

    class Meta:
        verbose_name = _('Лечение')
        verbose_name_plural = _('Виды лечения')

    def __str__(self) -> str:
        return str(self.name)


class InformationBlock(models.Model):
    title = models.TextField(
        verbose_name=_('Заголовок блока'),
    )
    information_markdown = models.TextField()
    information_html = models.TextField(editable=False)
    service = models.OneToOneField(
        to=Service,
        on_delete=models.CASCADE,
        related_name='information_set',
        related_query_name='information',
    )
