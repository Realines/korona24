from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import (
    HttpResponse,
    HttpRequest,
)

from .models import Employee


def employee(request: HttpRequest, employee_id: int) -> HttpResponse:
    """
    Функция-контроллер страницы сотрудинка.

    :param request: Объект запроса.
    :param employee_id: id сотрудника.
    :return: Объект ответа со страницей сотрудника.
    """

    current_employee = get_object_or_404(Employee, pk=employee_id)

    context = {
        'current_employee': current_employee,
    }

    return render(request=request,
                  template_name='employees/employee.html',
                  context=context)
