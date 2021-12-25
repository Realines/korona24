from typing import (
    Dict,
    Any,
)
from django.http import HttpRequest
from .models import SiteSettings


def get_site_settings(request: HttpRequest) -> Dict[str, Any]:
    return {'site_settings': SiteSettings.load()}
