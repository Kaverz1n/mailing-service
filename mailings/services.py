from django.conf import settings
from django.core.mail import send_mail


def send_email(title, body, users_email_list) -> None:
    '''
    Функция отправляет e-mail сообщение на указанную почту/ы
    :param title: имя сообщения
    :param body: тело сообщения
    :param users_email_list: список e-mail адресов получателей
    '''
    try:
        send_mail(
            title,
            body,
            settings.EMAIL_HOST_USER,
            users_email_list,
            fail_silently=False
        )
    except:
        print('Ошибка отправки')
