from django.shortcuts import render
from django.http import HttpResponse
from tasks import *
# Create your views here.


def index(request):
    send_mail_task.delay("Leave Application",
                         "Got Affected By Dengue",
                         "yamanswain@gmail.com",
                         ["hello@gmail.com","new@gmail.com"])
    return HttpResponse('Django-Celery')