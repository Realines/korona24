from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
)
from django.utils.translation import gettext as _

from services.models import Service
from employees.models import Employee
from comments.models import Comment
from gallery.models import Gallery
from .forms import ConsultationForm


def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.

    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """

    services_set = Service.objects.filter(show_on_main=True)
    gallery_set = Gallery.objects.all()[:6]
    employees_set = Employee.objects.all()
    comments_set = Comment.objects.filter(status=Comment.Status.APPROVED)

    context = {'services': services_set,
               'gallery': gallery_set,
               'employees': employees_set,
               'comments': comments_set}

    return render(request=request,
                  template_name='main/index.html',
                  context=context)


def consultation_handler(request: HttpRequest) -> JsonResponse:
    """
    Функция-контроллер для обработки форму консультации через AJAX.

    :param request: Объект запроса.
    :return: Возвращает статус обработки в формате JSON.
    """

    # Инициализируем форму данными из POST запроса в JSON-формате.
    form = ConsultationForm(request.POST)

    # Валидация формы, связанной с моделью.
    if form.is_valid():
        form.save()
    else:
        # Именованный параметр json_dumps_params нужен, чтобы на клиент корректно
        # отрпавлялись не только ascii символы, но и, например, китайские символы.
        return JsonResponse(data={'errors': form.errors,
                                  'msg': _('Form submission error')},
                            status=403,
                            json_dumps_params={'ensure_ascii': False})

    return JsonResponse(data={'msg': _('OK')},
                        status=201,
                        json_dumps_params={'ensure_ascii': False})


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


def about(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы "О нас".

    :param request: Объект запроса.
    :return: Объект ответа со страницей "О нас".
    """

    context = {}

    return render(request=request,
                  template_name='main/about.html',
                  context=context)
