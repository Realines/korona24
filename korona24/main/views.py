from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
)

from .models import Gallery
from services.models import Service
from employees.models import Employee
from comments.models import Comment


def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.

    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """

    # Получаем необязательный параметр из GET-запроса, отвечающий
    # за контроль стилей сайта
    visually_impaired_version = request.GET.get('visually_version', None)

    services_set = Service.objects.all()[:4]
    gallery_set = Gallery.objects.all()[:6]
    all_employees = Employee.objects.all()
    comments_set = Comment.objects.filter(status=Comment.Status.APPROVED)

    context = {'services': services_set,
               'gallery': gallery_set,
               'employees': all_employees,
               'comments': comments_set}

    return render(request=request,
                  template_name='main/index.html',
                  context=context)


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы контактов.

    :param request: Объект запроса.
    :return: Объект ответа со страницей контактов.
    """

    context = {}

    return render(request=request,
                  template_name='main/contacts.html',
                  context=context)


def gallery(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер галереи.

    :param request: Объект запроса.
    :return: Объект ответа со старницей галереи.
    """

    context = {}

    return render(request=request,
                  template_name='main/gallery.html',
                  context=context)
