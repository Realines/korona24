from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
)
from django.utils.translation import gettext as _

from .forms import CommentForm
from .models import Comment
from main.utility import application_send_mail

def comments(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы отзывов.

    :param request: Объект запроса.
    :return: Объект ответа со страницей отзывов.
    """

    comments_set = Comment.objects.filter(status=Comment.Status.APPROVED) 
    context = {'comments':comments_set}

    return render(request=request,
                  template_name='comments/comments.html',
                  context=context)


def comments_handler(request: HttpRequest) -> JsonResponse:
    """
    Функция-контроллер для обработки отправки формы отзыва.

    :param request: Объект запроса.
    :return: Объект ответа в формате JSON.
    """

    # Инициализируем форму данными из POST запроса в JSON-формате.
    form = CommentForm(request.POST)

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
    
    application_send_mail(f"Клиент: {form.cleaned_data['client_name']} Номер: {form.cleaned_data['phone_number']} Отзыв: {form.cleaned_data['text']}",'missis.korona@mail.ru', subject=f"Новый отзыв! Клиент: {form.cleaned_data['client_name']}")
    return JsonResponse(data={'msg': _('OK')},
                        status=201,
                        json_dumps_params={'ensure_ascii': False})
