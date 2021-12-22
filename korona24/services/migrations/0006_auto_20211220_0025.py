# Generated by Django 3.2.9 on 2021-12-19 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_informationservice_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, default='sys/service_icons/default.png', upload_to='sys/service_icons/', verbose_name='Иконка услуги')),
                ('name', models.TextField(verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('show_on_main', models.BooleanField(default=False, verbose_name='Показать на главной')),
            ],
            options={
                'verbose_name': 'Предпросмотр услуги на главной (4 блока)',
                'verbose_name_plural': 'Предпросмотр услуги',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='preview',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='services.previewservice', verbose_name='Превью для главной'),
            preserve_default=False,
        ),
    ]
