import math
import random
from itertools import chain
from functools import reduce
from typing import Optional

from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
)
from django.core.paginator import Paginator
from django.utils.translation import gettext as _
from django.views.decorators.csrf  import csrf_exempt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
import json
from .models import Category, Page  
from employees.models import Employee

def employees(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы "Списка сотрудников".

    :param request: Объект запроса.
    :return: Объект ответа со страницей "О нас".
    """
    all_category = Category.objects.all()
    employees_set = Employee.objects.all()
    all_pages = Page.objects.filter(show_on_main=True)
    context = { 
        'all_category': all_category,
        'all_pages': all_pages,
        'employees': employees_set
    } 

    return render(request=request,
                  template_name='pages/employes.html',
                  context=context)
def about(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы "О нас".

    :param request: Объект запроса.
    :return: Объект ответа со страницей "О нас".
    """
    all_category = Category.objects.all()
    all_pages = Page.objects.filter(show_on_main=True)
    context = { 
        'all_category': all_category,
        'all_pages': all_pages
    } 

    return render(request=request,
                  template_name='pages/about.html',
                  context=context)


def page(request: HttpRequest, page_title: str) -> HttpResponse:
    """
    Функция-контроллер шаблонной страницы.

    :param request: Объект запроса.
    :param page_title: Адрес шаблонной страницы.
    :return: Объект ответа со старницей статей.
    """

    current_page = get_object_or_404(Page, address=page_title)
    all_category = Category.objects.all()  
    all_pages = Page.objects.filter(show_on_main=True)
    context = {
        'current_page': current_page,
        'all_category': all_category,
        'all_pages': all_pages
    }

    return render(request=request,
                  template_name='pages/page.html',
                  context=context)
