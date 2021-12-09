from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
)


def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.

    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """

    # Получаем необязательный параметр из GET-запроса, отвечающий
    # за контроль стилей сайта
    visually_impaired_version = request.GET.get('visually_version', None)
    return render()


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы контактов.

    :param request: Объект запроса.
    :return: Объект ответа со страницей контактов.
    """

    return render()


def gallery(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер галереи.

    :param request: Объект запроса.
    :return: Объект ответа со старницей галереи.
    """

    return render()
