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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super().__init__(*args, **kwargs)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        is_existed = Client.objects.filter(email=cleaned_data, user=self.user).exists()

        if is_existed:
            raise forms.ValidationError('Пользователь с таким e-mail существует!')

        return cleaned_data
