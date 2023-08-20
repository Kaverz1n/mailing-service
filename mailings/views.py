from typing import Any

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from pytils.translit import slugify

from mailings.models import Mailing, MailingStatus, Client


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
    fields = ('title', 'body', 'sending_time', 'regularity',)
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            mailing = form.save()
            mailing.slug = slugify(f'{mailing.title}-{mailing.pk}')
            mailing.save()

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
    fields = ('title', 'body', 'sending_time', 'regularity',)
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            mailing = form.save()
            mailing.slug = slugify(f'{mailing.title}-{mailing.pk}')
            mailing.save()

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
    fields = ('fullname', 'email', 'comment',)
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
    fields = ('fullname', 'email', 'comment',)
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
