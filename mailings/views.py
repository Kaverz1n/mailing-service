from typing import Any

from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from pytils.translit import slugify

from mailings.models import Mailing


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


class MailingDeleteView(DeleteView):
    '''
    Класс для удаления рассылки
    '''
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')
