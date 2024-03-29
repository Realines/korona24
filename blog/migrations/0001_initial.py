# Generated by Django 3.2.9 on 2021-12-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(help_text='Будет использоваться в URL страницы.', verbose_name='Название страницы статьи')),
                ('title', models.TextField(verbose_name='Заголовок статьи')),
                ('description', models.TextField(help_text='Первый абзац статьи.', verbose_name='Описание')),
                ('image', models.ImageField(help_text='Будет отображаться в статье и в ее миниатюре в списке статей.', upload_to='sys/article_images/', verbose_name='Изображение статьи')),
                ('alt_image', models.TextField(verbose_name='Описание изображения')),
                ('information_markdown', models.TextField(help_text='Поддерживает markdown.', verbose_name='Основная информация')),
                ('information_html', models.TextField(editable=False)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
