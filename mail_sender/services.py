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
        except Exception:
            status = 'неудача'
            server_report = 'неизвестная ошибка'
        finally:
            MailingLog.objects.create(
                last_send=datetime.now(),
                status=status,
                server_report=server_report,
                clients=mailing_list.clients.all(),
                mailing_list=mailing_list
            )