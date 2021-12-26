from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.urls import reverse

from markdown import markdown
from blog.models import Article


class PreviewService(models.Model):
    icon = models.FileField(
        upload_to='sys/service_icons/',
        verbose_name=_('Иконка услуги'),
        default='sys/service_icons/default.png',
        blank=True,
    )
    alt_icon = models.TextField(
        verbose_name=_('Описание иконки'),
    )
    name = models.TextField(
        verbose_name=_('Название услуги'),
    )
    description = models.TextField(
        verbose_name=_('Описание услуги'),
    )
      
    show_on_main = models.BooleanField(
        verbose_name=_('Показать на главной'),
        default=False,
    )

    class Meta:
        verbose_name = _('Предпросмотр услуги на главной (4 блока)')
        verbose_name_plural = _('Предпросмотр услуги')

    def get_absolute_url(self) -> str:
        return reverse('services:service', args=(str(self.service.pk), ))

    def __str__(self) -> str:
        return str(self.name)


class ServiceArticle(models.Model):
    title = models.TextField(
        verbose_name=_('Заголовок статьи'),
    )
    description = models.TextField(
        verbose_name=_('Описание'),
        help_text=_('Первый абзац статьи'),
    )
    image = models.ImageField(
        upload_to='sys/article_images/',
        verbose_name=_('Изображение статьи'),
        help_text=_('Будет отображаться в статье и в '
                    'ее миниатюре в списке статей.'),
    )
    alt_image = models.TextField(
        verbose_name=_('Описание изображения'),
    )
    image_description = models.TextField(
        max_length=400,
        verbose_name=_('Описание изображение статьи'),
    )
    information_markdown = models.TextField(
        verbose_name=_('Основная информация'),
        help_text=_('Поддерживает markdown.'),
    )
    information_html = models.TextField(
        editable=False,
    )

    class Meta:
        verbose_name = _('Статья об услуги')
        verbose_name_plural = _('Статьи об услуги')

    def save(self, *args, **kwargs):
        self.information_html = markdown(self.information_markdown)
        super(ServiceArticle, self).save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse('services:article', args=(str(self.pk), ))
    
    def data_json(self):
        return {
            "id": self.pk,
            "title": self.title,
            "url": self.get_absolute_url(),
            "image_url": self.image.url,
            'description': self.description,
        }

    def __str__(self) -> str:
        return str(self.title)


class Service(models.Model):
    preview = models.OneToOneField(
        PreviewService,
        on_delete=CASCADE, 
        verbose_name=_('Превью для главной'),
        related_name='service'
    )
    name = models.TextField(
        verbose_name=_('Название услуги'),
    )
    description = models.TextField(
        verbose_name=_('Описание услуги'),
    )
    blog_articles = models.ManyToManyField(
        to=ServiceArticle,
        verbose_name=_('Статьи об услуги'),
        related_name='articles',
        related_query_name='articles',
    )
    title_price_block = models.TextField(
        verbose_name=_('Заголовок для блока цен'),
    )
    description_price_block = models.TextField(
        verbose_name=_('Описание для блока цен'),
    ) 

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def get_absolute_url(self) -> str:
        return reverse('services:service', args=(str(self.pk), ))

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
    description = models.TextField(
        verbose_name=_('Описание'),
        help_text=_('Необходимо для улучшения индексации страниц '
                    'поисковыми роботами.'),
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


class InformationService(models.Model):
    information_markdown = models.TextField(
        verbose_name=_('Дополнительная информация об услуге'),
        help_text=_('Поддерживает markdown.'),
    )
    information_html = models.TextField(
        editable=False,
    )
    service = models.OneToOneField(
        to=Service,
        on_delete=models.CASCADE,
        related_name='information',
        related_query_name='information',
    )

    class Meta:
        verbose_name = _('Дополнительная информация')
        verbose_name_plural = _('Дополнительная информация')

    def save(self, *args, **kwargs):
        self.information_html = markdown(self.information_markdown)
        super(InformationService, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Информация услуги {self.pk}'
