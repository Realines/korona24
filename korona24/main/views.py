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
