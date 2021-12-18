# Generated by Django 3.2.9 on 2021-12-18 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20211219_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='estimate',
            field=models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка клиента'),
        ),
    ]
