import re
from celery.decorators import task
from .email import send_review_email
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name='send_review_email_task')

def send_review_email_task(name, email, review):
    logger.info('Email review sent!')
    return send_review_email(name, email, review)