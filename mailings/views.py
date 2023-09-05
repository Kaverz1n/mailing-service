from typing import Any

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from pytils.translit import slugify

from mailings.forms import MailingForm, ClientForm
from mailings.models import Mailing, MailingStatus, Client, MailingLogs


class IndexView(TemplateView):
    '''
    Класс отображения главной страницы сервиса
    '''
    template_name = 'mailings/index.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

        return context


class MailingListView(ListView):
    '''
    Класс отображения страницы со всеми рассылками
    '''
    model = Mailing

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рассылки'

        return context


class MailingDetailView(DetailView):
    '''
    Класс для отображения информации об одной рассылке
    '''
    model = Mailing

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class MailingCreateView(CreateView):
    '''
    Класс для создания рассылки
    '''
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form) -> HttpResponse:
        if form.is_valid():
            self.object = form.save()
            self.object.slug = slugify(f'{self.object.title}-{self.object.pk}')
            self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание рассылки'

        return context


class MailingUpdateView(UpdateView):
    '''
    Класс для редактирования рассылки
    '''
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form) -> HttpResponse:
        if form.is_valid():
            self.object = form.save()
            self.object.slug = slugify(f'{self.object.title}-{self.object.pk}')
            self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование рассылки {self.object.title}'

        return context


class MailingDeleteView(DeleteView):
    '''
    Класс для удаления рассылки
    '''
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление рассылки {self.object.title}'

        return context


def change_status(request, slug) -> HttpResponse:
    '''
    Переводит рассылку к типу "завершена"
    '''
    object_id = Mailing.objects.get(slug=slug).pk
    object = get_object_or_404(Mailing, pk=object_id)

    if request.method == 'POST':
        object.status = MailingStatus.objects.get(name='завершена')
        object.save()
        return redirect('mailings:mailing_list')

    return render(request, 'mailings/mailing_status_change.html', {'object': object, 'title': 'Подтверждение'})


class ClientListView(ListView):
    '''
    Класс для отображения всех клиентов
    '''
    model = Client

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Клиенты'

        return context


class ClientDetailView(DetailView):
    '''
    Класс для отображения одного клиента
    '''
    model = Client

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.fullname

        return context


class ClientCreateView(CreateView):
    '''
    Класс для создания клиента
    '''
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание клиента'

        return context


class ClientUpdateView(UpdateView):
    '''
    Класс для обновления клиента
    '''
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование клиента {self.object.fullname}'

        return context


class ClientDeleteView(DeleteView):
    '''
    Класс для удаления клиента
    '''
    model = Client
    success_url = reverse_lazy('mailings:client_list')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление клиента {self.object.fullname}'

        return context


class MailingLogsListView(ListView):
    '''
    Класс для просмотра всех логов рассылок
    '''
    model = MailingLogs
    template_name = 'mailings/mailing_logs_list.html'

    def get_queryset(self, *args, **kwargs) -> MailingLogs:
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.order_by('-attempt_datetime')

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Логи рассылок'

        return context_data
