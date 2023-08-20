from django.contrib import admin

from mail_sender.models import Client, Settings


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)
    search_fields = ('name', 'email')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('time', 'frequency',)

