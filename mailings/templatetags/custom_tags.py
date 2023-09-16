from django import template
from django.conf import settings
from django.core.cache import cache

register = template.Library()


@register.filter
def mediapath(url) -> str:
    '''
    Возвращает созданный путь к изображениям
    в папке media
    :param url: url изображения
    :return: созданный путь
    '''
    media_url = f'/media/{url}'
    return media_url


@register.filter
def has_group(user, group_name) -> bool:
    '''
    Возвращает True, в случае если пользователь относится
    к определенной группе пользователей
    :param user: пользователь
    :param group_name: имя группы
    :return: bool-значение
    '''
    if settings.CACHE_ENABLED:
        cache_key = f'user_belongs_{user.pk}_{group_name}'
        users_group = cache.get(cache_key)
        if users_group is None:
            users_group = user.groups.filter(name=group_name).exists()
            cache.set(cache_key, users_group, 3600)

        return users_group

    return user.groups.filter(name=group_name).exists()
