from django.contrib import admin
from mdeditor.widgets import MDEditorWidget
from django.db import models as db_models

from . import models


@admin.register(models.ServiceArticle)
class ServiceArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', )
    formfield_overrides = {
        db_models.TextField: {'widget': MDEditorWidget},
    }


class TherapyInline(admin.StackedInline):
    model = models.Therapy
    extra = 0


class InformationServiceInline(admin.StackedInline):
    model = models.InformationService
    extra = 1
    formfield_overrides = {
        db_models.TextField: {'widget': MDEditorWidget},
    }


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', )
    inlines = [
        TherapyInline,
        InformationServiceInline,
    ]
    formfield_overrides = {
        db_models.TextField: {'widget': MDEditorWidget},
    }


@admin.register(models.PreviewService)
class PreviewServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', )
    formfield_overrides = {
        db_models.TextField: {'widget': MDEditorWidget},
    }
