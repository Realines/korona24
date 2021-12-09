from django.contrib import admin
from . import models


class TherapyInline(admin.StackedInline):
    model = models.Therapy


class InformationServiceInline(admin.StackedInline):
    model = models.InformationService


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', )
    inlines = [
        TherapyInline,
        InformationServiceInline,
    ]
