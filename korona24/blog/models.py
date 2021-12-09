from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
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
                    'ее миниатюре в списке статей.')
    )
    information_markdown = models.TextField(
        verbose_name=_('Основная информация'),
        help_text=_('Эта информация будет находится '
                    'после описания и изображения статьи.')
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

    def __str__(self) -> str:
        return str(self.title)
