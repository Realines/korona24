from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.urls import reverse 
from markdown import markdown
from main.utility import translify


class Category(models.Model):
    title = models.TextField(
        verbose_name=_('Заголовок категории'),
    )

    class Meta:
        verbose_name = _('Категории доп страниц')
        verbose_name_plural = _('Категории страниц')
        
    def get_absolute_url(self) -> str:
        firstPage = self.pages.all()[0]
        print(firstPage)
        return reverse('pages:page', args=(str(firstPage.address), ))
    def __str__(self) -> str:
        return str(self.title)


class Page(models.Model):
    category = models.ManyToManyField(
        Category,
        verbose_name=_('Превью для главной'),
        related_name='pages',
        blank=True,
    )
    address = models.TextField(
        verbose_name=_('Адресс страницы транскриптом')
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
        blank=True
    )
    image_description = models.TextField(
        max_length=400,
        verbose_name=_('Описание изображение статьи'),
        blank=True,
    )
    information_markdown = models.TextField(
        verbose_name=_('Основная информация'),
        help_text=_('Поддерживает markdown.'),
    )
    information_html = models.TextField(
        editable=False,
    )
    show_on_main = models.BooleanField(
        verbose_name=_('Страница в меню'),
        default=False,
    )
    show_on_website = models.BooleanField(
        verbose_name=_('Опубликовано?'),
        default=False,
    )

    class Meta:
        verbose_name = _('Шаблонная страница')
        verbose_name_plural = _('Страница')

    def save(self, *args, **kwargs):
        self.information_html = markdown(self.information_markdown)
        if(self.address is None):
            self.address = translify(self.title)
        super(Page, self).save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse('pages:page', args=(str(translify(self.title)), ))
     
    def __str__(self) -> str:
        return str(self.title)
