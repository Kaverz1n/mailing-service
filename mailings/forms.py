from django import forms

from mailings.models import Mailing, Client


class MailingForm(forms.ModelForm):
    '''
    Форма рассылки сервиса
    '''

    class Meta:
        model = Mailing
        fields = ('title', 'body', 'sending_time', 'regularity',)


class ClientForm(forms.ModelForm):
    '''
    Форма клиента сервиса
    '''

    class Meta:
        model = Client
        fields = ('fullname', 'email', 'comment',)
