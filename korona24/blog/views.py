from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
)
from django.core.paginator import Paginator

from .models import Article


def articles(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы статей.

    :param request: Объект запроса.
    :return: Объект ответа со старницей статей.
    """

    context = {}

    return render(request=request,
                  template_name='blog/blog.html',
                  context=context)


def article(request: HttpRequest, article_id: int) -> HttpResponse:
    """
    Функция-контроллер страницы статей.

    :param request: Объект запроса.
    :param article_id: id статьи.
    :return: Объект ответа со старницей статей.
    """

    context = {}

    return render(request=request,
                  template_name='blog/blog-item.html',
                  context=context)
