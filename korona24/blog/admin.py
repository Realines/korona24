from django.contrib import admin
from django.db import models as db_models
from mdeditor.widgets import MDEditorWidget
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', )
    formfield_overrides = {
        db_models.TextField: {'widget': MDEditorWidget}
    }
