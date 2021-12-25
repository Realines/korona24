from django.contrib import admin
from django.db.utils import ProgrammingError

from .models import (
    SiteSettings,
    SocialNetwork,
    PhoneAndAddress,
)


class SocialNetworkInline(admin.StackedInline):
    model = SocialNetwork


class PhoneAndAddressInline(admin.StackedInline):
    model = PhoneAndAddress


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
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
    inlines = (
        SocialNetworkInline,
        PhoneAndAddressInline,
    )

    def __init__(self, model, admin_site):
        """Инициализатор класса"""
        super().__init__(model, admin_site)

        # Создаем дефолтный экземпляр настроек при
        # первом запросе к странице с настройками.
        try:
            SiteSettings.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        """
        Метод проверки прав на добавление.
        По умолчанию запрещаем добавление новых записей.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Метод проверки прав на удаление.
        По умолчанию запрещаем удаление записей.
        """
        return False
