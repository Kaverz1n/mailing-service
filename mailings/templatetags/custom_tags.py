from django import template

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
    return user.groups.filter(name=group_name).exists()
