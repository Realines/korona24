from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import (
    HttpResponse,
    HttpRequest,
)

from .models import Employee


def employee(request: HttpRequest, employee_url: str) -> HttpResponse:
    """
    Функция-контроллер страницы сотрудинка.

    :param request: Объект запроса.
    :param employee_url: url сотрудника.
    :return: Объект ответа со страницей сотрудника.
    """

    current_employee = get_object_or_404(Employee, url=employee_url)
    employees_set = Employee.objects.all()

    context = {
        'current_employee': current_employee,
        'employees': employees_set,
    }

    return render(request=request,
                  template_name='employees/employee.html',
                  context=context)
