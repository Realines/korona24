from django.contrib import admin
from . import models


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('description', )
    list_display_links = ('description', )
