from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import (
    HttpResponse,
    HttpRequest,
    Http404,
)

from .models import Service, ServiceArticle,PreviewService

def services(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы услуг.

    :param request: Объект запроса.
    :return: Объект ответа со страницей услуг.
    """
    preview_services = PreviewService.objects.all()

    context = {'preview_services':preview_services}

    return render(request=request,
                  template_name='services/services.html',
                  context=context)


def service(request: HttpRequest, service_url: str) -> HttpResponse:
    """
    Функция-контроллер страницы услуги.

    :param request: Объект запроса.
    :param service_url: url услуги.
    :return: Объект ответа со страницей услуги.
    """

    current_service = get_object_or_404(Service, url=service_url)
    context = {
        'current_service': current_service,
    }

    return render(request=request,
                  template_name='services/service.html',
                  context=context)

def service_parrent_article(request: HttpRequest, service_url: str
                    ,parrent_url: str
                    ,article_url: str) -> HttpResponse:
    """
    Функция-контроллер страницы статьи об услуги.

    :param request: Объект запроса.
    :param service_url: url услуги.
    :param article_url: url статьи услуги.
    :return: Объект ответа со страницей услуги.
    """

    # Ищем статью с указанным url услуги и url самой статьи.
    current_article = ServiceArticle.objects.filter(service__url=service_url,
                                                    url=article_url).first()
    # Если такой статьи не нашлось - возвращаем 404.
    if current_article is None:
        raise Http404

    context = {
        'current_article': current_article,
    }

    return render(request=request,
                  template_name='services/service_article.html',
                  context=context)
 
def service_article(request: HttpRequest, service_url: str,
                    article_url: str) -> HttpResponse:
    """
    Функция-контроллер страницы статьи об услуги.

    :param request: Объект запроса.
    :param service_url: url услуги.
    :param article_url: url статьи услуги.
    :return: Объект ответа со страницей услуги.
    """

    # Ищем статью с указанным url услуги и url самой статьи.
    current_article = ServiceArticle.objects.filter(service__url=service_url,
                                                    url=article_url).first()
    # Если такой статьи не нашлось - возвращаем 404.
    if current_article is None:
        raise Http404

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

    context = {}

    return render(request=request,
                  template_name='services/price.html',
                  context=context)
