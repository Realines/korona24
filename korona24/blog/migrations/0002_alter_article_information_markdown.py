# Generated by Django 3.2.9 on 2021-12-09 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='information_markdown',
            field=models.TextField(help_text='Поддерживает markdown.', verbose_name='Основная информация'),
        ),
    ]