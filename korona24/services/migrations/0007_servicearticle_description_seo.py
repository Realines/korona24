# Generated by Django 3.2.9 on 2022-01-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_remove_servicearticle_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicearticle',
            name='description_seo',
            field=models.TextField(default='', verbose_name='Описание для SEO'),
            preserve_default=False,
        ),
    ]