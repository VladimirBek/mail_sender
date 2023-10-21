import smtplib
from datetime import timezone, datetime
from django.core.mail import send_mail

from config import settings
from .models import Mail, MailingList, MailingLog


def execute_mailing(mailing_list: MailingList):
    mails = Mail.objects.filter(mailing_list=mailing_list)
    for mail in mails:
        subject = mail.subject
        body = mail.body
        recipients_list = [rec.email for rec in mailing_list.clients.all()]
        status = 'успешно'
        server_report = None
        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipients_list,
                fail_silently=False
            )
            status = 'успешно'
            server_report = None
        except smtplib.SMTPException as error:
            status = 'неудача'
            server_report = error
        finally:
            instance = MailingLog.objects.create(
                last_send=datetime.now(timezone.utc),
                status=status,
                server_report=server_report,
                mailing_list=mailing_list
            )
            instance.clients.set(mailing_list.clients.all())


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




