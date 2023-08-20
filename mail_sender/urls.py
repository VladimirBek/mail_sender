from django.urls import path

from .apps import MailSenderConfig
from .views import IndexView, ClientsList, ClientDetail, ClientCreate, ClientUpdate, ClientDelete, MailingLists, \
    MailingDetail, MailingCreate, MailingUpdate, MailingDelete

app_name = MailSenderConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/', ClientsList.as_view(), name='clients_list'),
    path('client/<int:pk>', ClientDetail.as_view(), name='client_detail'),
    path('create_client', ClientCreate.as_view(), name='client_create'),
    path('update_client/<int:pk>', ClientUpdate.as_view(), name='client_update'),
    path('delete_client/<int:pk>', ClientDelete.as_view(), name='client_delete'),
    path('mailing_lists/', MailingLists.as_view(), name='mailing_list'),
    path('mailing_detail/<int:pk>', MailingDetail.as_view(), name='mailing_detail'),
    path('mailing_create/', MailingCreate.as_view(), name='mailing_create'),
    path('mailing_update/<int:pk>', MailingUpdate.as_view(), name='mailing_update'),
    path('mailing_delete/<int:pk>', MailingDelete.as_view(), name='mailing_delete'),

]
