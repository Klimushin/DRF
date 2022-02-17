import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
app = Celery('main')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-email-every-60-minutes': {
        'task': 'user.middleware.send_email_superuser',
        'schedule': crontab(minute='*/1'),
    },
}
