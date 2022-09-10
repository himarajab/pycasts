from celery import shared_task
from pprint import pprint

@shared_task()
def hello_celery():
    pprint('hello celery')