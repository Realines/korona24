from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
)


def services(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы услуг.

    :param request: Объект запроса.
    :return: Объект ответа со страницей услуг.
    """

    context = {}

    return render(request=request,
                  template_name='services.html',
                  context=context)


def service(request: HttpRequest, service_id: int) -> HttpResponse:
    """
    Функция-контроллер страницы услуги.

    :param request: Объект запроса.
    :param service_id: id услуги.
    :return: Объект ответа со страницей услуги.
    """

    context = {}

    return render(request=request,
                  template_name='service.html',
                  context=context)


def prices(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы цен на услуги.

    :param request: Объект запроса.
    :return: Объект ответа со страницей цен на услуги.
    """

    context = {}

    return render(request=request,
                  template_name='price.html',
                  context=context)
