from django.contrib.auth.models import User
from django.core.mail import send_mail

from api.viewsets import count_call_endpoint, average_request_time
from main.settings import FROM_EMAIL
from main.celery import app



@app.task
def send_email_superuser():
    email_list = [superusers.email for superusers in User.objects.filter(is_superuser=True)]

    send_mail(
        'Request report',
        f'Request count {count_call_endpoint}, request time {average_request_time}',
        FROM_EMAIL,
        email_list,
        fail_silently=False,
    )
