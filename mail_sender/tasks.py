from config.celery import app
from mail_sender.services import check_mailing_ready


@app.task
def repeat_check_mailing():
    check_mailing_ready()
