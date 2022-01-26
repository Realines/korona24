from django.contrib import admin

from .models import (
    SiteSetting, 
    PhoneAndAddres,
) 

admin.site.register(PhoneAndAddres)

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    """
    Класс регистарции настроек сайта.
    Для успешной миграции и регистрации этой модели в БД
    должна быть таблица common_info_sitesettings.
    """
    list_display = (
        'years_on_market',
        'count_operations',
        'count_doctors',
        'count_patients',
    )
    list_display_links = (
        'years_on_market',
        'count_operations',
        'count_doctors',
        'count_patients',
    )
    def has_add_permission(self, request, obj=None):
        """
        Метод проверки прав на добавление.
        По умолчанию запрещаем добавление новых записей.
        """
        return True

    def has_delete_permission(self, request, obj=None):
        """
        Метод проверки прав на удаление.
        По умолчанию запрещаем удаление записей.
        """
        return True
