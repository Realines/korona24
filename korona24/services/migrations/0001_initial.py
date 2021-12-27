# Generated by Django 3.2.9 on 2021-12-27 17:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(blank=True, default='sys/service_icons/default.png', upload_to='sys/service_icons/', verbose_name='Иконка услуги')),
                ('alt_icon', models.TextField(verbose_name='Описание иконки')),
                ('name', models.TextField(verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('show_on_main', models.BooleanField(default=False, verbose_name='Показать на главной')),
            ],
            options={
                'verbose_name': 'Предпросмотр услуги на главной (4 блока)',
                'verbose_name_plural': 'Предпросмотр услуги',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(help_text='Будет использоваться в URL страницы.', verbose_name='Название страницы услуги')),
                ('name', models.TextField(verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('title_price_block', models.TextField(verbose_name='Заголовок для блока цен')),
                ('description_price_block', models.TextField(verbose_name='Описание для блока цен')),
                ('preview', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='services.previewservice', verbose_name='Превью для главной')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('description', models.TextField(help_text='Необходимо для улучшения индексации страниц поисковыми роботами.', verbose_name='Описание')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapies', related_query_name='therapy', to='services.service')),
            ],
            options={
                'verbose_name': 'Лечение',
                'verbose_name_plural': 'Виды лечения',
            },
        ),
        migrations.CreateModel(
            name='ServiceArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(help_text='Будет использоваться в URL страницы.', verbose_name='Название страницы статьи')),
                ('title', models.TextField(verbose_name='Заголовок статьи')),
                ('description', models.TextField(help_text='Первый абзац статьи', verbose_name='Описание')),
                ('image', models.ImageField(help_text='Будет отображаться в статье и в ее миниатюре в списке статей.', upload_to='sys/article_images/', verbose_name='Изображение статьи')),
                ('alt_image', models.TextField(verbose_name='Описание изображения')),
                ('image_description', models.TextField(max_length=400, verbose_name='Описание изображение статьи')),
                ('information_markdown', models.TextField(help_text='Поддерживает markdown.', verbose_name='Основная информация')),
                ('information_html', models.TextField(editable=False)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_articles', related_query_name='service_article', to='services.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Статья об услуги',
                'verbose_name_plural': 'Статьи об услуги',
            },
        ),
        migrations.CreateModel(
            name='InformationService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_markdown', models.TextField(help_text='Поддерживает markdown.', verbose_name='Дополнительная информация об услуге')),
                ('information_html', models.TextField(editable=False)),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='information', related_query_name='information', to='services.service')),
            ],
            options={
                'verbose_name': 'Дополнительная информация',
                'verbose_name_plural': 'Дополнительная информация',
            },
        ),
    ]
