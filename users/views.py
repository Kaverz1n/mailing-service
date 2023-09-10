import string
import random

from typing import Any

from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, TemplateView

from mailings.services import send_email
from users.forms import RegisterForm, ResetPasswordForm
from users.models import User


class UserRegisterView(CreateView):
    '''
    Класс для регистрации пользователей
    '''
    model = User
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form) -> HttpResponse:
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.save()

            # генерация токена и uid зарегестрированого пользователя для его дальнейшей активации
            token = default_token_generator.make_token(self.object)
            uid = urlsafe_base64_encode(force_bytes(self.object.id))
            active_url = reverse_lazy('users:email_confirm', kwargs={'uidb64': uid, 'token': token})

            # отправка e-mail сообщения с ссылкой на активацию пользователя
            send_email(
                'Подтверждение e-mail адресса!',
                f'Чтобы подтвердить Ваш e-mail адрес, перейдите по ссылке: http://127.0.0.1:8000{active_url}',
                [self.object.email]
            )

            return redirect('users:email_sent_confirm')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Регистрация'

        return context_data


class UserConfirmEmailView(View):
    '''
    Класс для подтверждения e-mail адреса
    '''

    def get(self, request, uidb64, token) -> HttpResponse:
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except:
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            group = Group.objects.get(name='service_users')
            user.groups.add(group)
            user.is_active = True
            user.save()

            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_fail_confirm')


class UserSentConfirmEmail(TemplateView):
    '''
    Класс для отображения шаблона с успешной отправкой письма
    '''
    template_name = 'users/email_sent_confirm.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Письмо отрплавено'

        return context_data


class UserConfirmedEmail(TemplateView):
    '''
    Класс для отображения шаблона о подтверждении e-mail адреса
    '''
    template_name = 'users/email_confirmed.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'E-mail подтвержден'

        return context_data


class UserFailConfirmEmail(TemplateView):
    '''
    Класс для отображения шаблона об ошибке при подверждение e-mail адреса
    '''
    template_name = 'users/email_fail_confirm.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Ошибка подтверждения'

        return context_data


class UserLoginView(LoginView):
    '''
    Класс для авторизации пользователей
    '''
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Авторизация'

        return context_data


class UserPasswordResetView(View):
    '''
    Класс для сброса пароля пользователя сервиса
    '''

    def get(self, request) -> HttpResponse:
        form = ResetPasswordForm

        return render(request, 'users/password_reset_form.html', {'form': form})

    def post(self, request) -> HttpResponse:
        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            user = User.objects.get(email=request.POST.get('email'))
            symbols = string.ascii_letters + string.digits
            password = ''.join(str(random.choice(symbols)) for _ in range(10))
            user.set_password(password)
            user.save()

            send_email(
                'Ваш новый пароль!',
                f'Ваш пароль для входа в систему: {password}',
                [user.email]
            )

            return redirect('users:password_sent_email')

        return render(request, 'users/password_reset_form.html', {'form': form})


class UserSentPassword(TemplateView):
    '''
    Класс для отображения шаблона об успешной отправки нового пароля
    '''
    template_name = 'users/password_sent_email.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Новый пароль отправлен'

        return context_data
