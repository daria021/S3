from AbstractRepository import AbstractRepo
from .models import Newsletter
from newsletter.schemas import NewsletterUpdate, NewsletterCreate, NewsletterResponse


class NewsletterRepo(AbstractRepo):
    model = Newsletter
    update_schema = NewsletterUpdate
    create_schema = NewsletterCreate
    get_schema = NewsletterResponse
