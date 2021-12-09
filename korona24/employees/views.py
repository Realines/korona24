from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
)


def employee(request: HttpRequest, employee_id: int) -> HttpResponse:
    """
    Функция-контроллер страницы сотрудинка.

    :param request: Объект запроса.
    :param employee_id: id сотрудника.
    :return: Объект ответа со страницей сотрудника.
    """

    return render()
