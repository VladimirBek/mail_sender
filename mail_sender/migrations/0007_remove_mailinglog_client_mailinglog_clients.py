# Generated by Django 4.2.4 on 2023-08-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0006_alter_mailinglog_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailinglog',
            name='client',
        ),
        migrations.AddField(
            model_name='mailinglog',
            name='clients',
            field=models.ManyToManyField(to='mail_sender.client', verbose_name='клиент'),
        ),
    ]
