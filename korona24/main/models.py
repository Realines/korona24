from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators


class Employee(models.Model):
    name = models.TextField(
        verbose_name=_('Имя'),
    )
    position = models.TextField(
        verbose_name=_('Должность'),
    )
    work_schedule = models.TextField(
        verbose_name=_('График работы'),
    )
    avatar = models.ImageField(
        upload_to='sys/employee_avatars/',
        verbose_name=_('Аватар сотрудника'),
        default=...,  # TODO: Придумать дефолтную аватарку.
    )

    class Meta:
        verbose_name = _('Работник')
        verbose_name_plural = _('Работники')

    def __str__(self) -> str:
        return str(self.name)


class Education(models.Model):
    institution = models.TextField(
        verbose_name=_('Учебное заведение'),
    )
    start_study = models.IntegerField(
        verbose_name=_('Начало обучения'),
        validators=[validators.MinValueValidator(0)],
    )
    end_study = models.IntegerField(
        verbose_name=_('Конец обучения'),
        validators=[validators.MinValueValidator(0)],
    )
    specialization = models.TextField(
        verbose_name=_('Специализация'),
    )
    qualification = models.TextField(
        verbose_name=_('Квалификация'),
    )
    employee = models.OneToOneField(
        to=Employee,
        on_delete=models.CASCADE,
        related_name='educations',
        related_query_name='education',
    )

    class Meta:
        verbose_name = _('Образование')
        verbose_name_plural = _('Образования')

    def __str__(self) -> str:
        return str(self.institution)


class SkillDevelop(models.Model):
    year = models.IntegerField(
        verbose_name=_('Год повышения'),
        validators=[validators.MinValueValidator(0)],
    )
    name = models.TextField(
        verbose_name=_('Название квалификации'),
    )
    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE,
        related_name='skill_develops',
        related_query_name='skill_develop',
    )


class EmployeeInformation(models.Model):
    year = models.IntegerField(
        verbose_name=_('Год'),
        validators=[validators.MinValueValidator(0)],
    )
    text = models.TextField(
        verbose_name=_('Информация'),
    )
    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE,
        related_name='add_information_set',
        related_query_name='add_information',
    )

    class Meta:
        verbose_name = _('Дополнительная информация')
        verbose_name_plural = _('Дополнительная информация')

    def __str__(self) -> str:
        return str(self.text)
