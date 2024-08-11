import asyncio

from fastapi_mail import FastMail, MessageType, MessageSchema

from .mail_config import mail_conf
from .setup_celery import celery_app
import kombu.utils.json as json_utils


@celery_app.task()
def send_letter(message: str):
    data = json_utils.loads(message)
    data['subtype'] = MessageType.html
    message = MessageSchema.model_validate(data)
    fm = FastMail(mail_conf)
    asyncio.run(fm.send_message(message))
    print("Email sent")
    return
