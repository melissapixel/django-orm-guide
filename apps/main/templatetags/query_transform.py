from django import template # для создания пользовательских тегов и фильтров шаблонов
from django.http import QueryDict   # для работы с параметрами GET-запросов

register = template.Library()   # регистрируем библиотеку пользовательских тегов

@register.simple_tag
def url_replace(request, field, value):
    """
    Заменяет или добавляет параметр в GET-запросе.
    Пример: {% url_replace request 'page' 2 %}
    """
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()