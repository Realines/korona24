# Generated by Django 3.2.9 on 2021-12-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, default='comments/default.png', upload_to='comments/', verbose_name='Аватар клиента'),
        ),
    ]