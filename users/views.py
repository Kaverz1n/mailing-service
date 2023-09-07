from typing import Any

from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm
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
            self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Регистрация'

        return context_data


class UserLoginView(LoginView):
    '''
    Класс для авторизации пользователей
    '''
    template_name = 'users/authorization.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Авторизация'

        return context_data
