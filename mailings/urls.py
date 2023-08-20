from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import (
    IndexView, MailingListView, MailingDetailView, MailingCreateView,
    MailingUpdateView, MailingDeleteView, change_status, ClientListView,
    ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView
)

app_name = MailingsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<slug:slug>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing_update/<slug:slug>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_delete/<slug:slug>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('status_change/<slug:slug>/', change_status, name='mailing_status'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete')
]
