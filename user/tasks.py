from django.contrib.auth.models import User
from django.core.mail import send_mail

from main.settings import FROM_EMAIL
from main.celery import app
from user.models import DataForEmail


@app.task
def send_email_superuser():
    email_list = [superusers.email for superusers in User.objects.filter(is_superuser=True)]
    count_call_endpoint = DataForEmail.objects.first().request_count
    average_request_time = DataForEmail.objects.first().average_time

    send_mail(
        'Request report',
        f'Request count {count_call_endpoint}, request time {average_request_time}',
        FROM_EMAIL,
        email_list,
        fail_silently=False,
    )
