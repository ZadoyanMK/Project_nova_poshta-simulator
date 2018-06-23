from django.db import models

# Create your models here.


class User(models.Model):
    FIO = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    email = models.EmailField()


class Order(models.Model):
    weight = models.IntegerField(default=0)
    order_name = models.CharField(max_length=255)
    sender = models.ForeignKey(
        'User',
        related_name='Order_sender',
        on_delete=models.CASCADE,
    )
    getter = models.ForeignKey(
        'User',
        related_name='Order_getter',
        on_delete=models.CASCADE,

    )
    transporting = models.ForeignKey(
        'Transporting',
        related_name='Order_transporting',
        on_delete=models.CASCADE,
    )


class Transporting(models.Model):
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
    time_leaving = models.DateTimeField()


class Punkt(models.Model):
    location_name = models.CharField(max_length=255)
    location_x = models.FloatField(default=0)
    location_y = models.FloatField(default=0)


class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    speed = models.IntegerField()
    max_weight = models.IntegerField()
