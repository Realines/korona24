from django.contrib import admin
from . import models
from image_cropping import ImageCroppingMixin


class EducationInline(admin.StackedInline):
    model = models.Education
    extra = 0


class SkillDevelopInline(admin.StackedInline):
    model = models.SkillDevelop
    extra = 0


class EmployeeInfoInline(admin.StackedInline):
    model = models.EmployeeInfo
    extra = 0

 
@admin.register(models.Employee)
class EmployeeAdmin(ImageCroppingMixin,admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = ('name', )
    inlines = [
        EducationInline,
        SkillDevelopInline,
        EmployeeInfoInline,
    ]
