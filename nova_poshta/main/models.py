from django.db import models
from django.contrib.auth.models import User

from datetime import timedelta

# Create your models here.


class Messages(models.Model):
    user = models.ForeignKey(
        User,
        related_name='Message_getter',
        on_delete=models.CASCADE,
    )
    sender = models.CharField(max_length=60)
    text_message = models.TextField(max_length=255)

    def __str__(self):
        return 'Sender: %s, message: %s, getter: %s' % (
            self.text_message,
            self.user.username,
            self.sender
        )


class Order(models.Model):
    weight = models.IntegerField()
    order_name = models.CharField(max_length=100)
    sender = models.ForeignKey(
        User,
        related_name='Order_sender',
        on_delete=models.CASCADE,
    )
    getter_email = models.EmailField()
    getter_name = models.CharField(max_length=60)
    getter_surname = models.CharField(max_length=60)
    punkt_from = models.ForeignKey(
        'Punkt',
        on_delete=models.CASCADE,
        related_name='Transporting_punkt_from'
    )
    punkt_to = models.ForeignKey(
        'Punkt',
        on_delete=models.CASCADE,
        related_name='Transporting_punkt_to'
    )
    vehicle = models.ForeignKey(
        'Vehicle',
        on_delete=models.CASCADE,
        related_name='Transporting_vehicle',
        null=True,
    )

    STATUS_CREATING = 0
    STATUS_SENDED = 100
    STATUS_SENDING = 80
    STATUS_SEARCHING_FOR_TRANSPORT = 25
    STATUS_WAITING_FOR_TRANSPORTING = 60
    STATUSES = (
        (STATUS_CREATING, 'Creating'),
        (STATUS_SENDED, 'Sended'),
        (STATUS_SENDING, 'Sending'),
        (STATUS_SEARCHING_FOR_TRANSPORT, 'Searching for transport'),
        (STATUS_WAITING_FOR_TRANSPORTING, 'Waiting for transporting'),
    )
    status = models.SmallIntegerField(choices=STATUSES, default=STATUS_CREATING)

    def __str__(self):
        return 'Order: %s, from %s to %s, sender: %s, getter: %s' % (
            self.order_name,
            self.punkt_from.location_name,
            self.punkt_to.location_name,
            self.sender.username,
            self.getter_name + ' ' + self.getter_surname
        )


class Punkt(models.Model):
    location_name = models.CharField(max_length=100)
    location_x = models.FloatField()
    location_y = models.FloatField()

    def __str__(self):
        return '%s' % self.location_name


class Vehicle(models.Model):
    
    time_leaving = models.DateTimeField()
    time_arrival = models.DateTimeField()
    name = models.CharField(max_length=100)
    max_weight = models.IntegerField()
    total_weight = models.IntegerField(default=0)
    punkt_to = models.ForeignKey(
        'Punkt',
        on_delete=models.CASCADE,
        related_name='Vehicle_punkt_to'
    )
    punkt_where_staying = models.ForeignKey(
        'Punkt',
        on_delete=models.CASCADE,
        related_name='Vehicle_punkt_where_staying'
    )

    STATUS_STOPPED = 0
    STATUS_MOVING = 100
    STATUSES = (
        (STATUS_STOPPED, 'Waiting for moving'),
        (STATUS_MOVING, 'Moving'),
    )
    status = models.SmallIntegerField(choices=STATUSES, default=STATUS_STOPPED)

    def __str__(self):
        return 'Name - %s, weight - %s, staying in %s, going to %s' % (
            self.name,
            self.max_weight,
            self.punkt_where_staying,
            self.punkt_to
        )
