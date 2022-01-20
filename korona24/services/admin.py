from django.contrib import admin
from . import models  
from mdeditor.widgets import MDEditorWidget
from django.db import models as db_models


@admin.register(models.ServiceArticle)
class ServiceArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', )
    formfield_overrides = {
        db_models.TextField: {'widget': MDEditorWidget}
    }


class TherapyInline(admin.StackedInline):
    model = models.Therapy
    extra = 0

 

admin.site.register(models.PreviewService) 

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', )
    inlines = [
        TherapyInline, 
    ] 
    formfield_overrides = {
        db_models.TextField: {'widget': MDEditorWidget}
    }
