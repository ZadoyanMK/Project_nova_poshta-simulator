from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.core.mail import send_mail

from celery import shared_task
from celery import task
from .models import Messages, Vehicle, Order

from datetime import datetime, timedelta
from django.utils import timezone


@shared_task
def message_creating(sender_id, getter_id, order_name):
    message1 = Messages(
        user=User.objects.get(id=sender_id),
        sender='Nova_poshta_information',
        text_message='Your order ' + order_name + ' creates',
    )
    message1.save()

    message2 = Messages(
        user=User.objects.get(id=getter_id),
        sender='Nova_poshta_information',
        text_message='Your order ' + order_name + ' creates',
    )
    message2.save()
    # Отправка сообщений на почту, ошибка: ConnectionRefusedError: [Errno 111] Connection refused
    # как это исправить?
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'konzamir@gmail.com',
    #     ['konzamir@gmail.com'],
    #     fail_silently=False,
    # )

    return 'send message wen order created'


@shared_task
def message_creating_with_new_user(sender_id, getter_id, order_name):
    message1 = Messages(
        user=User.objects.get(id=sender_id),
        sender='Nova_poshta_information',
        text_message='Your order ' + order_name + ' creates',
    )
    message1.save()

    message2 = Messages(
        user=User.objects.get(id=getter_id),
        sender='Nova_poshta_information',
        text_message='Welcome to Nova Poshta, your password is 123',
    )
    message2.save()

    message3 = Messages(
        user=User.objects.get(id=getter_id),
        sender='Nova_poshta_information',
        text_message='Your order ' + order_name + ' creates',
    )
    message3.save()

    return 'send message wen order created with creating user'


@task
def search_vehicle():
    orders = Order.objects.filter(status=Order.STATUS_SEARCHING_FOR_TRANSPORT)
    found = False
    for ord in orders:
        vehicles = Vehicle.objects.filter(
            status=Vehicle.STATUS_STOPPED,
            punkt_where_staying=ord.punkt_from,
            punkt_to=ord.punkt_to,
        )
        for veh in vehicles:
            if veh.max_weight > ord.weight + veh.total_weight:
                Vehicle.objects.filter(
                    id=veh.id
                ).update(total_weight=veh.total_weight + ord.weight)
                Order.objects.filter(
                    id=ord.id
                ).update(
                    status=Order.STATUS_WAITING_FOR_TRANSPORTING,
                    vehicle=veh,
                )
                sender = ord.sender

                message = Messages(
                    user=User.objects.get(id=sender.id),
                    sender='Nova_poshta_information',
                    text_message='Your order %s founds the vehicle' % ord.order_name,
                )
                message.save()
                found = True
    return found


@task
def start_transporting():
    vehicles = Vehicle.objects.filter(status=Vehicle.STATUS_STOPPED)
    now = timezone.now()
    found = False
    for veh in vehicles:
        if veh.time_leaving < now:
            print('found')
            found = True
            Vehicle.objects.filter(
                id=veh.id
            ).update(status=Vehicle.STATUS_MOVING)
            orders = Order.objects.filter(vehicle=veh, status=Order.STATUS_WAITING_FOR_TRANSPORTING)

            for ord in orders:
                Order.objects.filter(
                    id=ord.id
                ).update(status=Order.STATUS_SENDING)

                sender = ord.sender

                getter = User.objects.filter(
                    first_name=ord.getter_name,
                    last_name=ord.getter_surname,
                    email=ord.getter_email,
                ).first()

                message1 = Messages(
                    user=User.objects.get(id=sender.id),
                    sender='Nova_poshta_information',
                    text_message='Your order %s is sending' % ord.order_name,
                )
                message1.save()

                message2 = Messages(
                    user=User.objects.get(id=getter.id),
                    sender='Nova_poshta_information',
                    text_message='Your order %s is sending' % ord.order_name,
                )
                message2.save()
    return found


@task
def stop_transporting():
    vehicles = Vehicle.objects.filter(status=Vehicle.STATUS_MOVING)

    found = False
    now = timezone.now()
    for veh in vehicles:
        if veh.time_arrival < now:
            found = True
            punkt = veh.punkt_to
            Vehicle.objects.filter(
                id=veh.id
            ).update(
                status=Vehicle.STATUS_STOPPED,
                time_leaving=datetime.now() + timedelta(hours=5),
                time_arrival=veh.time_arrival + timedelta(hours=5),
                punkt_to=veh.punkt_where_staying,
                punkt_where_staying=punkt,
            )
            orders = Order.objects.filter(vehicle=veh, status=Order.STATUS_SENDING)

            for ord in orders:
                Order.objects.filter(
                    id=ord.id
                ).update(status=Order.STATUS_SENDED)

                sender = ord.sender

                getter = User.objects.filter(
                    first_name=ord.getter_name,
                    last_name=ord.getter_surname,
                    email=ord.getter_email,
                ).first()
                message1 = Messages(
                    user=User.objects.get(id=sender.id),
                    sender='Nova_poshta_information',
                    text_message='Your order %s was sended' % ord.order_name,
                )
                message1.save()

                message2 = Messages(
                    user=User.objects.get(id=getter.id),
                    sender='Nova_poshta_information',
                    text_message='Your order %s was sended' % ord.order_name,
                )
                message2.save()
    return found
