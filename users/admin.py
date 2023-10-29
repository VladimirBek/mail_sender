from django.contrib import admin

from users.models import User


@admin.register(User)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
