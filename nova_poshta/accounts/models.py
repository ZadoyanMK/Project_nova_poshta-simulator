from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Messages(models.Model):
    message = models.TextField()
    getter = models.ForeignKey(
        User,
        related_name='getter',
        on_delete=models.CASCADE,
    )
