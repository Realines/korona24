# Generated by Django 3.2.9 on 2021-12-26 15:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_on_market', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Лет на рынке')),
                ('count_operations', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Кол-во операций под общим наркозом')),
                ('count_doctors', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Кол-во профессиональных врачей')),
                ('count_patients', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Кол-во пацинатов в год')),
                ('enabled_partners', models.BooleanField(default=False, help_text='Включает или отключает блок партнеров на сайте.', verbose_name='Отображать партнеров')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='sys/social_networks_icons', verbose_name='Иконка социальной сети')),
                ('name', models.TextField(verbose_name='Название соц. сети')),
                ('url', models.URLField(verbose_name='Ссылка на соц. сеть')),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_networks', related_query_name='social_network', to='common_info.sitesettings')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.CreateModel(
            name='PhoneAndAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('phone_number', models.TextField(verbose_name='Номер телефона')),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_and_address_set', related_query_name='phone_and_address', to='common_info.sitesettings')),
            ],
            options={
                'verbose_name': 'Телефон и адрес',
                'verbose_name_plural': 'Телефоны и адреса',
            },
        ),
    ]
