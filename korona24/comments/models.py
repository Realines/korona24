from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators


class Comment(models.Model):
    class Status(models.TextChoices):
        ON_MODERATION = 'OM', 'На модерации'
        REJECTED = 'R', 'Отклонено'
        APPROVED = 'A', 'Одобрено'

    client_name = models.CharField(
        max_length=128,
        verbose_name=_('Имя клиента'),
    )
    phone_number = models.CharField(  # TODO: Найти хороший способ валидации номеров.
        max_length=16,
        verbose_name=_('Номер телефона'),
    )
    image = models.ImageField(
        upload_to='comments/',
        verbose_name=_('Аватар клиента'),
        default='comments/default.png',
        blank=True,
    )
    title = models.CharField(
        max_length=30,
        verbose_name=_('Заголовок комментария клиента'),
    )
    text = models.TextField(
        verbose_name=_('Комментарий клиента'),
    )
    estimate = models.SmallIntegerField(
        verbose_name=_('Оценка клиента'),
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(5)],
        null=True,
        blank=True,
    )
    date_added = models.DateField(
        verbose_name=_('Дата добавления отзыва'),
        auto_now_add=True,
    )
    status = models.CharField(
        max_length=2,
        verbose_name=_('Статус комментария'),
        choices=Status.choices,
        default=Status.ON_MODERATION,
    )
    def get_estimate_to_list(self):
        fackes_list = []
        for i in range(self.estimate):
            fackes_list.append('1')
        return fackes_list
    class Meta:
        verbose_name = _('Отзывы')
        verbose_name_plural = _('Отзывы')
        ordering = ['-date_added']
        get_latest_by = 'date_added'

    def __str__(self) -> str:
        return f'{self.client_name}#{self.pk}'
