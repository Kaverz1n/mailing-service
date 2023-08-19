import datetime

from mailing_service.settings import EMAIL_HOST_USER

from django.core.mail import send_mail
from django.db.models import Q

from mailings.models import Mailing, MailingStatus, MailingLogs, MailingRegularity


def send_email():
    '''
    Функция отправляет e-mail рассылку всем пользователям в указанную
    дату с определенной часттой - раз в день, раз в неделю, раз в месяц
    или единоразово. При единоразовой отправке, статус рассылки меняется
    на "завершенный". При первой отправке рассылки с указаной частотой,
    рассылка переходит на статус "запущена". После каждой рассылки с
    указанной частотой, дата следующей отправки увеличивается на указанный
    срок (день, 7 дней, 30 дней). После каждой рассылки, её логи сохраняются
    и помещаются в базу данных.
    '''
    now = datetime.datetime.now()
    mailings = Mailing.objects.filter(
        Q(status=MailingStatus.objects.get(name='создана')) |
        Q(status=MailingStatus.objects.get(name='запущена'))
    )
    admin_email = EMAIL_HOST_USER

    # перебор всех рассылок со статусом "создана" или "запущена"
    for mailing in mailings:
        try:
            # отправка e-mail рассылки, если настоящее время больше установленного для отправки
            if mailing.sending_time.timestamp() < now.timestamp():
                send_mail(mailing.title, mailing.body, admin_email, ['kaptan.alex@yandex.ru'],
                          fail_silently=False)
                MailingLogs.objects.create(mailing=mailing)

                # изменение статуса рассылки на "запущена", если у нее имеется частота отправки
                if mailing.regularity:
                    mailing.status = MailingStatus.objects.get(name='запущена')
                    mailing.save()
                    # увелечение даты следующей отправки
                    if mailing.regularity == MailingRegularity.objects.get(name='раз в день'):
                        mailing.sending_time += datetime.timedelta(days=1)
                    elif mailing.regularity == MailingRegularity.objects.get(name='раз в неделю'):
                        mailing.sending_time += datetime.timedelta(days=7)
                    else:
                        mailing.sending_time += datetime.timedelta(days=30)
                else:
                    mailing.status = MailingStatus.objects.get(name='завершена')

                mailing.save()
        except:
            MailingLogs.objects.create(mailing=mailing, status=False)
