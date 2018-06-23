from django.db import models

# Create your models here.


class Client(models.Model):
    FIO = models.CharField()
    phone_number = models.CharField()
    location = models.CharField()
    email = models.EmailField()


class Order(models.Model):
    order_name = models.CharField(max_length=255)
    sender = models.ForeignKey(
        'Client',
        related_name='Order_sender',
        on_delete=models.CASCADE,
    )
    getter = models.ForeignKey(
        'Client',
        related_name='Order_getter',
        on_delete=models.CASCADE,
    )
    transporting = models.ForeignKey(
        'Transporting',
        related_name='Order_getter',
        on_delete=models.CASCADE,
    )