from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators


class Comment(models.Model):
    client_name = models.CharField(
        max_length=128,
        verbose_name=_('Имя клиента'),
    )
    image = models.ImageField(
        upload_to='comments/',
        verbose_name=_('Аватар клиента'),
        default='comments/default.png',
        blank=True,
    )
    text = models.TextField(
        verbose_name=_('Комментарий клиента'),
    )
    estimate = models.SmallIntegerField(
        verbose_name=_('Оценка клиента'),
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(5)],
    )
    date_added = models.DateField(
        verbose_name=_('Дата добавления отзыва'),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
        ordering = ['-date_added']
        get_latest_by = 'date_added'

    def __str__(self) -> str:
        return f'{self.client_name}#{self.pk}'
