from django.db.models.signals import post_save

from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings


def userCreated(sender, instance, created, **kwargs):
    if created:
        user = instance
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )


post_save.connect(userCreated, sender=User)