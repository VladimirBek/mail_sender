from django.core.management import BaseCommand, CommandError

from mail_sender.models import MailingList
from mail_sender.services import execute_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        mailing_lists = MailingList.objects.all().filter(status='запущена')
        for mailing_list in mailing_lists:
            try:
                execute_mailing(mailing_list=mailing_list)
            except Exception as err:
                raise CommandError(f'Рассылку с названием "{mailing_list.name}" не удалось запустить. Ошибка: {err}')
