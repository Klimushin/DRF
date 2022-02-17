from django.utils.deprecation import MiddlewareMixin
from .tasks import send_email_superuser


class SendEmailMiddleware(MiddlewareMixin):
    # send_email_superuser()
    send_email_superuser.delay()
