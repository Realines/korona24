# Generated by Django 3.2.9 on 2021-12-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='gallery/default.png', upload_to='gallery/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание изображения')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Галерея',
            },
        ),
    ]
