from celery import Celery
from celery.utils.log import get_task_logger
from .email import send_review_email
import logging

logger = logging.getLogger(__name__)

app = Celery()

@app.task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    logger.info("sent review email")
    return send_review_email(name, email, review)