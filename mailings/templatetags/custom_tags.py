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
