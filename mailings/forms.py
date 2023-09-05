import re

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

    def clean_email(self) -> str:
        cleaned_data = self.cleaned_data['email']

        if not re.match(r'^[a-zA-Z0-9._]+@yandex\.ru$', cleaned_data):
            raise forms.ValidationError('Пользователь должен иметь почтовый ящик yandex.ru!')

        return cleaned_data
