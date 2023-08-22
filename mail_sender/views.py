from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DeleteView, CreateView, UpdateView, DetailView

from mail_sender.models import Client, MailingList, Mail


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

    def get_context_data(self, **kwargs):
        context = super(ClientDetail, self).get_context_data(**kwargs)
        ml = [str(item) for item in MailingList.objects.filter(clients=self.object)]
        context['mailing_lists'] = ', '.join(ml)
        return context


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


class MailList(ListView):
    model = Mail
    template_name = 'mail_list.html'


class MailDetail(DetailView):
    model = Mail
    template_name = 'mail_detail.html'


class MailCreate(CreateView):
    model = Mail
    template_name = 'mail_form.html'
    fields = ('subject', 'body', 'mailing_list',)
    success_url = reverse_lazy('mail_sender:mail_list')


class MailUpdate(UpdateView):
    model = Mail
    template_name = 'mail_form.html'
    fields = ('subject', 'body', 'mailing_list',)

    def get_success_url(self):
        return reverse('mail_sender:mail_detail', args=[self.object.pk])


class MailDelete(DeleteView):
    model = Mail
    template_name = 'mail_delete.html'
    success_url = reverse_lazy('mail_sender:mail_list')
