# from celery.task import Task
# # from celery.app.registry import absolute_import
#
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
#
# from django.core.mail import send_mail, EmailMultiAlternatives
# from celery import Celery
#
# app = Celery('accounts.tasks', broker='redis:`//localhost:6379/0')
#
#
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
#
#
# app.tasks.register(SignUp)
#
#
# @app.task
# def order_create(user):
#     pass
# #
# # from __future__ import absolute_import, unicode_literals
# # import random
# # # from celery. import task
# # from .celery import app
# #
# #
# # @app.task(name="sum_two_numbers")
# # def add(x, y):
# #     return x + y
# #
# #
# # @app.task(name="multiply_two_numbers")
# # def mul(x, y):
# #     total = x * (y * random.randint(3, 100))
# #     return total
# #
# #
# # @app.task(name="sum_list_numbers")
# # def xsum(numbers):
# #     return sum(numbers)
