from celery import Celery

from config import config

celery_app = Celery('celery', broker=config.redis_url)

celery_app.autodiscover_tasks(['celery_task.tasks'])
