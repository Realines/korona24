from django.contrib import admin 
from . import models
from mdeditor.widgets import MDEditorWidget
from django.db import models as db_models


@admin.register(models.Page)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', )
    formfield_overrides = {
        db_models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register(models.Category)
