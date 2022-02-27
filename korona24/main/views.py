from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse, 
)
from django.utils.translation import gettext as _
from .models import *
from services.models import Service,PreviewService
from employees.models import Employee
from comments.models import Comment
from gallery.models import Gallery
from .forms import ConsultationForm
from .utility import application_send_mail
from datetime import datetime 

def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.

    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """
    all_discount = Discount.objects.all()
    all_services = Service.objects.all()
   
    preview_services = PreviewService.objects.all()
    gallery_set = Gallery.objects.all()[:6]
    employees_set = Employee.objects.all()
    comments_set = Comment.objects.filter(status=Comment.Status.APPROVED) 
    context = {'all_discount': all_discount.filter(show_on_main=True),
               'main_services': preview_services.filter(show_on_main=True)[:4],
               'all_services': all_services,
              
               'gallery': gallery_set,
               'employees': employees_set,
               'comments': comments_set}

    return render(request=request,
                  template_name='main/index.html',
                  context=context)

def robots(request):
    return render( request=request,template_name='main/robots.txt', content_type="text/plain")

def sitemap(request):
    return render( request=request,template_name='main/sitemap.xml', content_type="text/xml")

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
                              

    application_send_mail(f"Клиент: {form.cleaned_data['client_name']} Номер: {form.cleaned_data['phone_number']} Дата заявки: {datetime.now()}",'missis.korona@mail.ru')
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


