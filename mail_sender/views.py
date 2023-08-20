from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DeleteView, CreateView, UpdateView, DetailView

from mail_sender.models import Client, MailingList


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Mail Sender Plus'
    }


class ClientsList(ListView):
    model = Client
    template_name = 'clients_list.html'


class ClientDetail(DetailView):
    model = Client
    template_name = 'client_detail.html'


class ClientCreate(CreateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    template_name = 'client_create.html'
    success_url = reverse_lazy('mail_sender:clients_list')


class ClientUpdate(UpdateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    template_name = 'client_create.html'

    def get_success_url(self):
        return reverse('mail_sender:client_detail', args=[self.object.pk])


class ClientDelete(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('mail_sender:clients_list')


class MailingLists(ListView):
    model = MailingList
    template_name = 'mailing_list.html'


class MailingDetail(DetailView):
    model = MailingList
    template_name = 'mailing_detail.html'


class MailingCreate(CreateView):
    model = MailingList
    template_name = 'mailing_form.html'
    fields = ('name', 'settings', 'settings', 'clients')
    success_url = reverse_lazy('mail_sender:mailing_list')


class MailingUpdate(UpdateView):
    model = MailingList
    template_name = 'mailing_form.html'
    fields = ('name', 'settings', 'settings', 'status', 'clients')

    def get_success_url(self):
        return reverse('mail_sender:mailing_detail', args=[self.object.pk])


class MailingDelete(DeleteView):
    model = MailingList
    template_name = 'mailing_delete.html'
    success_url = reverse_lazy('mail_sender:mailing_list')
