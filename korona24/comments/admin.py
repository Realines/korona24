from django.contrib import admin
from . import models


class CommentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'text', 'status')
    list_display_links = ('client_name', 'status')
    ordering = ('-date_added', '-estimate')
