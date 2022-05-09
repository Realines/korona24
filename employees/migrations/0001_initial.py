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
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(help_text='Будет использоваться в URL страницы.', verbose_name='Название страницы сотрудника')),
                ('description', models.TextField(help_text='Необходимо для улучшения индексации страниц поисковыми роботами.', verbose_name='Описание страницы сотрудника')),
                ('name', models.TextField(verbose_name='Имя')),
                ('position', models.TextField(verbose_name='Должность')),
                ('work_schedule', models.TextField(verbose_name='График работы')),
                ('avatar', models.ImageField(blank=True, default='sys/employee_avatars/default.png', upload_to='sys/employee_avatars/', verbose_name='Аватар сотрудника')),
                ('alt_avatar', models.TextField(verbose_name='Описание аватара')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='SkillDevelop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Год повышения')),
                ('name', models.TextField(verbose_name='Название квалификации')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_develops', related_query_name='skill_develop', to='employees.employee')),
            ],
            options={
                'verbose_name': 'Повышение квалификации',
                'verbose_name_plural': 'Повышения квалификаций',
            },
        ),
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Год')),
                ('text', models.TextField(verbose_name='Информация')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_information_set', related_query_name='add_information', to='employees.employee')),
            ],
            options={
                'verbose_name': 'Дополнительная информация',
                'verbose_name_plural': 'Дополнительная информация',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.TextField(verbose_name='Учебное заведение')),
                ('start_study', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Год начала обучения')),
                ('end_study', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Год окончания обучения')),
                ('specialization', models.TextField(verbose_name='Специализация')),
                ('qualification', models.TextField(verbose_name='Квалификация')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='education', related_query_name='education', to='employees.employee')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образования',
            },
        ),
    ]