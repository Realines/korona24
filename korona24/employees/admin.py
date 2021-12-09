from django.contrib import admin
from . import models


class EducationInline(admin.StackedInline):
    model = models.Education


class SkillDevelopInline(admin.StackedInline):
    model = models.SkillDevelop


class EmployeeInfoInline(admin.StackedInline):
    model = models.EmployeeInfo


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = ('name', )
    inlines = [
        EducationInline,
        SkillDevelopInline,
        EmployeeInfoInline,
    ]
