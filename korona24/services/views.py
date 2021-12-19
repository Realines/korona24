from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import (
    HttpResponse,
    HttpRequest,
)

from .models import Service


def services(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы услуг.

    :param request: Объект запроса.
    :return: Объект ответа со страницей услуг.
    """

    context = {}

    return render(request=request,
                  template_name='services/services.html',
                  context=context)


def service(request: HttpRequest, service_id: int) -> HttpResponse:
    """
    Функция-контроллер страницы услуги.

    :param request: Объект запроса.
    :param service_id: id услуги.
    :return: Объект ответа со страницей услуги.
    """

    current_service = get_object_or_404(Service, pk=service_id)

    context = {
        'current_service': current_service,
    }

    return render(request=request,
                  template_name='services/service.html',
                  context=context)


def prices(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы цен на услуги.

    :param request: Объект запроса.
    :return: Объект ответа со страницей цен на услуги.
    """

    context = {}

    return render(request=request,
                  template_name='services/price.html',
                  context=context)
