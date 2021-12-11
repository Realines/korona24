from django.http import (
    HttpRequest,
    HttpResponseRedirect,
)


def set_visually_version(request: HttpRequest,
                         visually_version: int) -> HttpResponseRedirect:
    """
    Функция-контроллер для смены версии сайта: обычный или для слабовидящих.

    :param request: Объект запроса.
    :param visually_version: Версия сайта. 1 - для слабовидящих, 0 - обычная версия.
    :return: Объект ответа с редиректом на ту же страницу.
    """

    # Меняем флаг версии сайта.
    # Стили сайта поменяются при рендеринге шаблона, который будет
    # использовать этот флаг. Это обеспечит соответствующая функция-middleware,
    # которая будет вызываться в context_processors.
    request.session['visually_impaired'] = True if visually_version == 1 else False

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
