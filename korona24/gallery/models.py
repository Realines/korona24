from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators


class Gallery(models.Model):
    image = models.ImageField(
        upload_to='gallery/',
        verbose_name=_('Изображение'),
        default='gallery/default.png',
        blank=True,
    )
    description = models.TextField(
        verbose_name=_('Описание изображения'),
    )

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Галерея')

    def __str__(self) -> str:
        return f'Image#{self.pk}'
        
    def data_json(self):
        return { "id":self.pk, "image_url":self.image.url,"description":self.description}
