# Generated by Django 4.2.4 on 2023-08-20 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_sender', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailinglist',
            old_name='client',
            new_name='clients',
        ),
    ]
