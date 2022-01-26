from typing import (
    Dict,
    Any,
)
from django.http import HttpRequest
from .models import Service


def get_all_services(request: HttpRequest) -> Dict[str, Any]:
    """
    Функция добавления в контекст каждого шаблона списка
    всех услуг. Необходимо для отображения услуг в шапке сайта,
    которая есть на каждой странице.

    :param request: Объект запроса.
    :return: Список услуг, которые будут добавлены в контекст.
    """

    all_services = Service.objects.all()
    footer_services =  Service.objects.all()[:5]
    footer_services_2 = []
    for service in all_services:
        if(service not in footer_services): 
            footer_services_2.append(service) 
    return {'all_services': all_services,
            'footer_services': footer_services,
            'footer_services_2': footer_services_2,}
