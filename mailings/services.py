from django.conf import settings
from django.core.mail import send_mail

from mailings.models import MailingStatus


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
    except Exception as e:
        print(
            'Ошибка отправки\n'
            f'Ошибка: {e}'
        )


def check_user(user, current_user) -> bool:
    '''
    Функция проверяет, что пользователь объекта является
    текущим, чтобы видеть страницу объекта, иначе переходит на другую
    страницу
    :param user: пользователь объекта
    :param current_user: текущий пользователь
    :return: bool
    '''
    return user == current_user


def check_mailing_status(mailing, status_name) -> bool:
    '''
    Функция проверят, что статус рассылки равен переданому
    :param mailing: рассылка сервиса
    :param status_name: имя статуса
    :return:
    '''
    status = MailingStatus.objects.get(name=status_name)

    return mailing.status == status
