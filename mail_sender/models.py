from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.EmailField(max_length=200, unique=True, verbose_name='email')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Settings(models.Model):
    class Frequency(models.TextChoices):
        DAILY = 'ежедневно'
        WEEKLY = 'еженедельно'
        MONTHLY = 'ежемесячно'

    class Status(models.TextChoices):
        DONE = 'завершена'
        CREATED = 'создана'
        LAUNCHED = 'запущена'
    time = models.TimeField(verbose_name='время рассылки', default='09:00:00')
    frequency = models.CharField(max_length=15, choices=Frequency.choices, default=Frequency.WEEKLY,
                                 verbose_name='периодичность')
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.CREATED, verbose_name='статус')


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема письма')

