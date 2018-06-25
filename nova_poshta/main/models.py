from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
        related_name='Transporting_vehicle'
    )
    completed = models.BooleanField(default=False)

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
    time_leaving = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    speed = models.IntegerField()
    max_weight = models.IntegerField()
    max_way = models.IntegerField()

    def __str__(self):
        return 'Name - %s, weight - %s' % (self.name, self.max_weight)
