from celery.task import Task
from celery.app.registry import absolute_import

from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import send_mail, EmailMultiAlternatives
from celery import Celery

app = Celery('accounts.tasks', broker='redis:`//localhost:6379/0')


# class SignUp(Task):
#     def run(self, user):
#
#         subject = "THellod"
#         from_email = "konzamir@gmail.com"
#         to_email = [user.email]
#         singup_message = """Hello new usen"""
#
#         send_mail(
#             subject=subject,
#             from_email=from_email,
#             recipient_list=to_email,
#             message=singup_message,
#             fail_silently=False
#         )


# app.tasks.register(SignUp)


@app.task
def order_create(user):
    pass