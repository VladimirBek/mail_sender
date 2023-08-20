# Generated by Django 4.2.4 on 2023-08-19 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название рассылки')),
                ('status', models.CharField(choices=[('завершена', 'Done'), ('создана', 'Created'), ('запущена', 'Launched')], default='создана', max_length=15, verbose_name='статус')),
                ('client', models.ManyToManyField(to='mail_sender.client')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default='09:00:00', verbose_name='время рассылки')),
                ('frequency', models.CharField(choices=[('ежедневно', 'Daily'), ('еженедельно', 'Weekly'), ('ежемесячно', 'Monthly')], default='еженедельно', max_length=15, verbose_name='периодичность')),
            ],
            options={
                'verbose_name': 'настройка рассылки',
                'verbose_name_plural': 'настройки рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_send', models.DateTimeField(verbose_name='последняя попытка')),
                ('status', models.CharField(choices=[('успешно', 'Success'), ('неудача', 'Fail')], default='неудача', max_length=10, verbose_name='статус попытки')),
                ('server_report', models.TextField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail_sender.mailinglist', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'лог рассылки',
                'verbose_name_plural': 'логи рассылки',
            },
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail_sender.settings', verbose_name='настройки рассылки'),
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='тема письма')),
                ('body', models.TextField(blank=True, null=True, verbose_name='тело письма')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail_sender.mailinglist', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'письмо',
                'verbose_name_plural': 'письма',
            },
        ),
    ]