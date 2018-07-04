from __future__ import absolute_import, unicode_literals
from .models import Messages
from celery import Task
# from celery.app.registry import

# @shared_task
# def create_order(user):
#     Messages.objects.create(
#         user=user,
#         sender='admin',
#         text_message='Order created'
#     )


class Hello(Task):
    queue = 'hipri'

    def run(self, to):
        return 'hello {0}'.format(to)

tasks.register(Hello)