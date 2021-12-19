# Generated by Django 3.2.9 on 2021-12-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20211220_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previewservice',
            name='icon',
            field=models.FileField(blank=True, default='sys/service_icons/default.png', upload_to='sys/service_icons/', verbose_name='Иконка услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='blog_articles',
            field=models.ManyToManyField(related_name='articles', related_query_name='articles', to='services.ServiceArticle', verbose_name='Статьи об услуги'),
        ),
    ]