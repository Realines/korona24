# Generated by Django 3.2.9 on 2021-12-16 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_service_description_price_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationservice',
            name='service',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='information', related_query_name='information', to='services.service'),
        ),
    ]