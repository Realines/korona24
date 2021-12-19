from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import (
    HttpResponse,
    HttpRequest,
)

from .models import Service, ServiceArticle


def services(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы услуг.

    :param request: Объект запроса.
    :return: Объект ответа со страницей услуг.
    """
    services = Service.objects.all()
    context = {
        'services': services
    }

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

def service_article(request: HttpRequest, article_id: int) -> HttpResponse:
    """
    Функция-контроллер страницы статьи об услуги.

    :param request: Объект запроса.
    :param service_id: id услуги.
    :return: Объект ответа со страницей услуги.
    """

    current_article = get_object_or_404(ServiceArticle, pk=article_id)

    context = {
        'current_article': current_article,
    }

    return render(request=request,
                  template_name='services/service_article.html',
                  context=context)

def prices(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы цен на услуги.

    :param request: Объект запроса.
    :return: Объект ответа со страницей цен на услуги.
    """
    services = Service.objects.all()
    context = {
        'services': services
    }

    return render(request=request,
                  template_name='services/price.html',
                  context=context)
