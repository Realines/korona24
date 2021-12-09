from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
)

from .models import Article


def test(request):
    return render(
        request=request,
        template_name='test.html',
        context={'articles': Article.objects.all()}
    )


def articles(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы статей.

    :param request: Объект запроса.
    :return: Объект ответа со старницей статей.
    """

    return render()


def article(request: HttpRequest, article_id: int) -> HttpResponse:
    """
    Функция-контроллер страницы статей.

    :param request: Объект запроса.
    :param article_id: id статьи.
    :return: Объект ответа со старницей статей.
    """

    return render()
