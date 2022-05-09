import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.urls import reverse

from markdown import markdown


class Article(models.Model):
    url = models.TextField(
        verbose_name=_('Название страницы статьи'),
        help_text=_('Будет использоваться в URL страницы.'),
    )
    title = models.TextField(
        verbose_name=_('Заголовок статьи'),
    )
    description = models.TextField(
        verbose_name=_('Описание'),
        help_text=_('Первый абзац статьи.'),
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
    information_markdown = models.TextField(
        verbose_name=_('Основная информация'),
        help_text=_('Поддерживает markdown.'),
    )
    information_html = models.TextField(
        editable=False,
    )

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    def save(self, *args, **kwargs):
        self.information_html = markdown(self.information_markdown)
        super(Article, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        os.remove(settings.BASE_DIR / self.image)
        return super(Article, self).delete(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse('blog:article', args=(str(self.url), ))
    
    def data_json(self):
        return {
            'id': self.pk,
            'title': self.title,
            'url': self.get_absolute_url(),
            'image_url': self.image.url,
            'alt_image': self.alt_image,
            'description': self.description
        }
    def __str__(self) -> str:
        return str(self.title)
