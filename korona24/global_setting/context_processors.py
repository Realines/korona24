from typing import (
    Dict,
    Any,
)
from django.http import HttpRequest
from .models import SiteSetting


def get_site_settings(request: HttpRequest) -> Dict[str, Any]:
    return {'site_settings': SiteSetting.objects.first()}

