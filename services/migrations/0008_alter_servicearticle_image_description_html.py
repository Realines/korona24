# Generated by Django 4.0.3 on 2022-04-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_servicearticle_image_description_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearticle',
            name='image_description_html',
            field=models.TextField(editable=False),
        ),
    ]
