from django.contrib import admin
from . import models

@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', )
    ordering = ('-date_added', )
    
@admin.register(models.Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'phone_number')
    list_display_links = ('client_name', )
    ordering = ('-date_added', )
