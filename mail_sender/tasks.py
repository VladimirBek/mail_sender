from datetime import datetime, timezone

from mail_sender.models import MailingList, MailingLog
from mail_sender.services import execute_mailing
from celery import shared_task


@shared_task
def check_mailing_ready():
    active_mailing = MailingList.objects.filter(status='запущена')
    for mailing_list in active_mailing:
        mailing_time = mailing_list.settings.time
        if mailing_time <= datetime.now().time():
            last_log = MailingLog.objects.filter(mailing_list=mailing_list).order_by('pk').last()
            if last_log:
                last_send = last_log.last_send
                time_now = datetime.now(timezone.utc)
                frequency = mailing_list.settings.frequency
                diff = time_now - last_send
                if frequency == 'ежедневно' and diff >= 1:
                    execute_mailing(mailing_list)
                elif frequency == 'еженедельно' and diff >= 7:
                    execute_mailing(mailing_list)
                elif frequency == 'ежемесячно' and diff >= 30:
                    execute_mailing(mailing_list)
            else:
                pass
