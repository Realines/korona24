from django.contrib import admin

from .models import (
    SiteSettings,
    SocialNetwork,
    PhoneAndAddress,
)
from utils.models.singleton_model import SingletonModelAdmin


class SocialNetworkInline(admin.StackedInline):
    model = SocialNetwork
    extra = 0


class PhoneAndAddressInline(admin.StackedInline):
    model = PhoneAndAddress
    extra = 0


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
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
