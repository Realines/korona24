from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.urls import reverse

from markdown import markdown


class Article(models.Model):
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

    def get_absolute_url(self) -> str:
        return reverse('blog:article', args=(str(self.pk), ))
    
    def data_json(self):
        return { "id":self.pk, "title":self.title,"url": self.get_absolute_url(), "image_url":self.image.url,'description':self.description}
    def __str__(self) -> str:
        return str(self.title)
