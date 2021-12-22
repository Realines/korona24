from typing import (
    Dict,
    Any,
)
from django.http import HttpRequest


def visually_impaired(request: HttpRequest) -> Dict[str, Any]:
    """
    Функция промежуточного ПО для определения версии запрашиваемой
    страницы: обычная или для слабовидящих.
    Используется в context_processors.

    :param request:
        Объект запроса. Из него будет извлекаться параметр
        версии страницы. Если такой есть - True, иначе False.
    :return: Словарь добавляемых значений в контекст шаблона.
    """

    # Получаем флаг версии сайта из сессии гостя сайта.
    visually_impaired_param: bool = request.session.get('visually_impaired', False)

    return {'visually_impaired': visually_impaired_param}
