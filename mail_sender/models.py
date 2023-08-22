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

    time = models.TimeField(verbose_name='время рассылки', default='09:00:00')
    frequency = models.CharField(max_length=15, choices=Frequency.choices, default=Frequency.WEEKLY,
                                 verbose_name='периодичность')

    def __str__(self):
        return f'Периодичность: {self.frequency}, время: {self.time}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'


class MailingList(models.Model):
    class Status(models.TextChoices):
        DONE = 'завершена'
        CREATED = 'создана'
        LAUNCHED = 'запущена'

    name = models.CharField(max_length=100, verbose_name='название рассылки')
    settings = models.ForeignKey(Settings, verbose_name='настройки рассылки', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.CREATED, verbose_name='статус')
    clients = models.ManyToManyField(Client, verbose_name='клиенты')

    def get_clients(self):
        return ', '.join([str(c) for c in self.clients.all()])

    def __str__(self):
        return f'{self.name} ({self.status})'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Mail(models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма', **NULLABLE)
    mailing_list = models.ManyToManyField(MailingList, verbose_name='рассылка')

    def get_mailing_lists(self):
        return '", "'.join([str(m) for m in self.mailing_list.all()])

    def __str__(self):
        return f'Письмо: {self.subject}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class MailingLog(models.Model):
    class Status(models.TextChoices):
        SUCCESS = 'успешно'
        FAIL = 'неудача'

    last_send = models.DateTimeField(verbose_name='последняя попытка', auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, verbose_name='статус попытки')
    server_report = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)
    client = models.ForeignKey(Client, verbose_name='клиент', on_delete=models.CASCADE)
    mailing_list = models.ForeignKey(MailingList, verbose_name='рассылка', on_delete=models.CASCADE)

    def __str__(self):
        return f'последняя попытка: {self.last_send}, статус: {self.status}, рассылка{self.mailing_list}'

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'
