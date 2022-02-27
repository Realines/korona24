
from re import T
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.urls import reverse
from mdeditor.fields import MDTextField
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
    def get_title_span(self):
        title_words = self.name.split('\n')
        #print(title_words)
        for i in range(len(title_words)):
            if(i > 0):
                title_words[i] = f" <span>{title_words[i]}</span>"
       
        title_small = '\n'.join(title_words) 
        #print(title_small.split(' '))
        return title_small 
    class Meta:
        verbose_name = _('Предпросмотр услуги на главной (4 блока)')
        verbose_name_plural = _('Предпросмотр услуги')

    def get_absolute_url(self) -> str:
        #return reverse('services:service', args=(str('/lechenie-zubov/') ))
        return ''

    def __str__(self) -> str:
        return str(self.name)


class ServiceArticle(models.Model):
    url = models.TextField(
        verbose_name=_('Название страницы статьи'),
        help_text=_('Будет использоваться в URL страницы.'),
    )
    title = models.TextField(
        verbose_name=_('Заголовок статьи'),
    )
    description = MDTextField(
        verbose_name=_('Описание'),
        help_text=_('Первый абзац статьи'),
    )

    title_seo = models.TextField(
        verbose_name=_('Заголовок статьи для SEO'),
        null=True,
        blank=True
    )
    description_seo = models.TextField(
        verbose_name=_('Описание для SEO'),
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
    information_markdown = MDTextField(
        verbose_name=_('Основная информация'),
        help_text=_('Поддерживает markdown.'),
    )
    information_html = models.TextField(
        editable=False,
    ) 
    parrent = models.ForeignKey(
        to='ServiceArticle',
        on_delete=models.CASCADE,
        verbose_name=_('Главная статья (Не обязательно)'),
        null=True,
        blank=True
    )
    service = models.ForeignKey(
        to='Service',
        on_delete=models.CASCADE,
        related_name='service_articles',
        related_query_name='service_article',
        verbose_name=_('Услуга'),
    )
    
    class Meta:
        verbose_name = _('Статья об услуги')
        verbose_name_plural = _('Статьи об услуги')

    def save(self, *args, **kwargs):
        self.information_html = markdown(self.information_markdown)
        self.description = markdown(self.description)
        if(len(self.title_seo) == 0):
            self.title_seo = self.title
        super(ServiceArticle, self).save(*args, **kwargs)
    def get_title_small(self):
        title_small = self.title.replace('В КРАСНОЯРСКЕ','').lower()
        title_small = title_small.replace('в красноярске','')
        title_small = title_small.replace('полости рта','')
        return title_small.capitalize()
    def get_absolute_url(self) -> str:
        if(self.parrent is None):
            return reverse('services:article',
                        args=(str(self.service.url), str(self.url), )) 
        else: 
            return reverse('services:parrent',
                        args=(str(self.service.url), str(self.parrent.url), str(self.url)))
        
    def data_json(self):
        return {
            'id': self.pk,
            'title': self.title,
            'url': self.get_absolute_url(),
            'image_url': self.image.url,
            'alt_image': self.alt_image,
            'description': self.description,
        }

    def __str__(self) -> str:
        return str(self.title)


class Service(models.Model):
    url = models.TextField(
        verbose_name=_('Название страницы услуги'),
        help_text=_('Будет использоваться в URL страницы.'),
    )
    preview = models.OneToOneField(
        PreviewService,
        on_delete=CASCADE, 
        verbose_name=_('Превью для главной'),
        related_name='service'
    )
    name = MDTextField(
        verbose_name=_('Название услуги'),
    )
    name_seo = models.TextField(
        verbose_name=_('Заголовок статьи для SEO'),
        null=True,
        blank=True
    )
    description = MDTextField(
        verbose_name=_('Описание услуги для SEO'),
    )
    text = MDTextField(
        verbose_name=_('Текст услуги'),
    )
    title_price_block = models.TextField(
        verbose_name=_('Заголовок для блока цен'),
    )
    description_price_block = MDTextField(
        verbose_name=_('Описание для блока цен'),
    )

    information_markdown = MDTextField(
        verbose_name=_('Дополнительная информация об услуге'), 
    )
    information_html = models.TextField(
        editable=False,
    )
    def save(self, *args, **kwargs):
        self.information_markdown = markdown(self.information_markdown)
        self.text = markdown(self.text)
        self. description_price_block = markdown(self. description_price_block)
        if(len(self.name) == 0):
            self.name_seo = self.name
        super(Service, self).save(*args, **kwargs)
    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')
    def get_title_small(self):
        title_small = self.name.replace('В КРАСНОЯРСКЕ','').lower()
        title_small = title_small.replace('в красноярске','')
        title_small = title_small.replace('полости рта','')
        return title_small.capitalize()
    def get_articles_for_menu(self) -> str:
        return self.service_articles.all()[:1]
    def get_absolute_url(self) -> str:
        return reverse('services:service', args=(str(self.url), ))

    def __str__(self) -> str:
        return str(self.name)


class Therapy(models.Model):
    name = models.TextField(
        verbose_name=_('Название'),
    )
    price = models.CharField(
        verbose_name=_('Цена'),
        max_length=10, 
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
 
