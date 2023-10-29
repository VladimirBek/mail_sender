from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DeleteView, CreateView, UpdateView, DetailView

from blog.models import BlogPost
from mail_sender.models import Client, MailingList, Mail


class IndexView(LoginRequiredMixin, TemplateView):
    total_mailings_count = MailingList.objects.count()
    active_mailings_count = MailingList.objects.filter(status='запущена').count()
    unique_clients_count = Client.objects.count()
    active_posts = BlogPost.objects.filter(is_active=True)
    ## Проверка на количество случайных постов, при значении ниже 3 выводятся все посты на главную страницу
    if active_posts.count() >= 3:
        random_posts = sample(list(active_posts), 3)
    else:
        random_posts = active_posts

    template_name = 'index.html'
    extra_context = {
        'title': 'Mail Sender Plus',
        'total_mailings_count': total_mailings_count,
        'active_mailings_count': active_mailings_count,
        'unique_clients_count': unique_clients_count,
        'random_posts': random_posts
    }




class ClientsList(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients_list.html'


class ClientDetail(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClientDetail, self).get_context_data(**kwargs)
        ml = [str(item) for item in MailingList.objects.filter(clients=self.object)]
        context['mailing_lists'] = ', '.join(ml)
        return context


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    template_name = 'client_create.html'
    success_url = reverse_lazy('mail_sender:clients_list')


class ClientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    permission_required = 'mail_sender.change_client'
    template_name = 'client_create.html'

    def get_success_url(self):
        return reverse('mail_sender:client_detail', args=[self.object.pk])


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    permission_required = 'mail_sender.delete_client'
    success_url = reverse_lazy('mail_sender:clients_list')


class MailingLists(LoginRequiredMixin, ListView):
    model = MailingList
    template_name = 'mailing_list.html'


class MailingDetail(LoginRequiredMixin, DetailView):
    model = MailingList
    template_name = 'mailing_detail.html'


class MailingCreate(LoginRequiredMixin, CreateView):
    model = MailingList
    template_name = 'mailing_form.html'
    fields = ('name', 'settings', 'settings', 'clients')
    success_url = reverse_lazy('mail_sender:mailing_list')


class MailingUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MailingList
    template_name = 'mailing_form.html'
    permission_required = 'mail_sender.change_mailing_list'
    fields = ('name', 'settings', 'settings', 'status', 'clients')

    def get_success_url(self):
        return reverse('mail_sender:mailing_detail', args=[self.object.pk])


class MailingDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MailingList
    template_name = 'mailing_delete.html'
    permission_required = 'mail_sender.delete_mailing_list'
    success_url = reverse_lazy('mail_sender:mailing_list')


class MailList(LoginRequiredMixin, ListView):
    model = Mail
    template_name = 'mail_list.html'


class MailDetail(LoginRequiredMixin, DetailView):
    model = Mail
    template_name = 'mail_detail.html'


class MailCreate(LoginRequiredMixin, CreateView):
    model = Mail
    template_name = 'mail_form.html'
    fields = ('subject', 'body', 'mailing_list',)

    success_url = reverse_lazy('mail_sender:mail_list')


class MailUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mail
    template_name = 'mail_form.html'
    permission_required = 'mail_sender.change_mail'
    fields = ('subject', 'body', 'mailing_list',)

    def get_success_url(self):
        return reverse('mail_sender:mail_detail', args=[self.object.pk])


class MailDelete(LoginRequiredMixin, DeleteView):
    model = Mail
    template_name = 'mail_delete.html'
    permission_required = 'mail_sender.delete_mail'
    success_url = reverse_lazy('mail_sender:mail_list')
