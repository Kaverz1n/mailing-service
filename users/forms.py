from django.contrib.auth.forms import UserCreationForm

from users.models import User


class RegisterForm(UserCreationForm):
    '''
    Форма регистрации пользователей сервиса
    '''

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
