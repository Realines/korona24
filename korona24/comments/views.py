from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
)


def comments(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы отзывов.

    :param request: Объект запроса.
    :return: Объект ответа со страницей отзывов.
    """

    return render()
