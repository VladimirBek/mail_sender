from django.contrib import admin

from mail_sender.models import Client, Settings, MailingList, Mail, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment',)
    search_fields = ('id', 'name', 'email')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'frequency',)


@admin.register(MailingList)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'settings', 'get_clients',)
    list_filter = ('status', 'clients')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'get_mailing_lists',)
    list_filter = ('mailing_list',)


@admin.register(MailingLog)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_send', 'status', 'server_report', 'client', 'mailing_list',)
