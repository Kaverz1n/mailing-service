from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import (
    IndexView, MailingListView, MailingDetailView, MailingCreateView,
    MailingUpdateView, MailingDeleteView
)

app_name = MailingsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<slug:slug>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('update/<slug:slug>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<slug:slug>/', MailingDeleteView.as_view(), name='mailing_delete')
]
