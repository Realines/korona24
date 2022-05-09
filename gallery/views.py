import math

from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest,
    JsonResponse,
)
from django.utils.translation import gettext as _
from django.core.paginator import Paginator

from .models import Gallery


def gallery(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер галереи.

    :param request: Объект запроса.
    :return: Объект ответа со старницей галереи.
    """

    context = {}

    return render(request=request,
                  template_name='gallery/gallery.html',
                  context=context)


def pagination_gallery(request: HttpRequest) -> JsonResponse:
    """
    Функция-контроллер для пагинации по галерее.
    :param request: Объект запроса.
    :return: Возвращает список ссылок на изображеня.
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
    gallery_set = Gallery.objects.all()
    block_image = 6
    paginator = Paginator(gallery_set, block_image)

    # Проверка, что номер запрашиваемого блока входит в длину пагинатора.
    if page_num < 1 or page_num > int(math.ceil(len(gallery_set) / block_image)):
        return JsonResponse(data={'errors': _('Error page number.')},
                            status=403)

    # Формирования списка url изображений.
    images = []
    for gallery_image in paginator.get_page(page_num).object_list: 
        images.append(gallery_image.data_json())

    return JsonResponse(
        data={'images': images,
              'max_pages': paginator.num_pages},
        status=200
    )
