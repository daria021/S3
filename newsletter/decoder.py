import kombu.utils.json as json_utils
from fastapi_mail import MessageSchema

from newsletter.schemas import NewsletterCreate


class MessageSchemaEncoder(json_utils.JSONEncoder):
    def default(self, o):
        if isinstance(o, MessageSchema):
            return {
                "subject": o.subject,
                "recipients": o.recipients,
                "body": o.body,
                "subtype": o.subtype.value,
            }
        if isinstance(o, NewsletterCreate):
            return {
                "subject": o.subject,
                "recipients": o.recipients,
                "body": o.body,
            }
        return super().default(o)
