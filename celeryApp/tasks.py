from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from time import sleep
import time
from django.core.mail import send_mail

# @shared_task
# def sleepy(duration):
#     sleep(duration)
#     return None
@shared_task
def sum(a,b):
    # time.sleep(10)
    return a+b

@shared_task
def send_email(email):
    #send_mail(subject="leave application", message='sir i am not feeling well today', recipient_list={email})
    print(f'A sample message is sent to {email}')

@shared_task
def send_mail_task(subject, message, email_from, recepient_list):
    msg = EmailMessage(subject, message, email_from, recepient_list)
    msg.content_subtype = 'html'
    msg.send()
