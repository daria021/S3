from newsletter.decoder import MessageSchemaEncoder
from newsletter.dependencies.repositories import mail_repo_context
from newsletter.schemas import NewsletterCreate
from celery_task.tasks import send_letter
import kombu.utils.json as json_utils


class MailService:
    async def send_mail(self, mail: NewsletterCreate):
        result = send_letter.apply_async((json_utils.dumps(mail, cls=MessageSchemaEncoder),))
        print("SXCVGLIUKFJGFHXDPLBK<MJNBFDZCVFGO", result)
        async with mail_repo_context() as mails:
            return await mails.create(mail)
