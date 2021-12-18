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
from django.core import serializers
from django.db.models import Q

from .models import Article


def articles(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер страницы статей.

    :param request: Объект запроса.
    :return: Объект ответа со старницей статей.
    """

    context = {}

    return render(request=request,
                  template_name='blog/blog.html',
                  context=context)


def pagination_articles(request: HttpRequest) -> JsonResponse:
    """
    Функция-контроллер для пагинации по статьям блога.
    :param request: Объект запроса.
    :return: Возвращает сериализованный в JSON список статей.
    """

    page_num = request.POST.get('page_num', None)

    # Проверка номера запрашиваемого блока с изображениями.
    if page_num is None:
        return JsonResponse(data={'errors': _('Error page number.')},
                            status=403)
    if page_num.isdigit():
        page_num = int(page_num)
    else:
        page_num = 1

    # Разбивка изображений на блоки в пагинаторе.
    article_set = Article.objects.all()
    block_articles = 6
    paginator = Paginator(article_set, block_articles)

    # Проверка, что номер запрашиваемого блока входит в длину пагинатора.
    if page_num < 1 or page_num > int(math.ceil(len(article_set) / block_articles)):
        return JsonResponse(data={'errors': _('Error page number.')},
                            status=403)

    # Сериализация списка объектов в JSON-формат.
    json_article_set = serializers.serialize('json', paginator.get_page(page_num).object_list)

    return JsonResponse(data={'articles': json_article_set},
                        status=200)


def article(request: HttpRequest, article_id: int) -> HttpResponse:
    """
    Функция-контроллер страницы статей.

    :param request: Объект запроса.
    :param article_id: id статьи.
    :return: Объект ответа со старницей статей.
    """

    # Текущая статья.
    current_article = get_object_or_404(Article, pk=article_id)

    # Генерируем рандомную подборку статей.
    # Получаем список id всех статей.
    all_articles_id = list(chain(*Article.objects.values_list('id')))
    count_articles = 3 if len(all_articles_id) > 3 else len(all_articles_id)

    # Перемешиваем id'шники и берем первые 3 (либо сколько есть).
    random.shuffle(all_articles_id)
    articles_id_set = all_articles_id[:count_articles]

    # Строим запрос на выборку рандомных статей.
    random_article = Article.objects.filter(pk__in=articles_id_set)

    context = {
        'current_article': current_article,
        'articles_set': random_article,
    }

    return render(request=request,
                  template_name='blog/blog-item.html',
                  context=context)
