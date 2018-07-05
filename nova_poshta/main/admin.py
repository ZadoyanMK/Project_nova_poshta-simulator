from django.contrib import admin
from .models import Punkt, Vehicle, Order, Messages
# Register your models here.

admin.site.register(Punkt)
admin.site.register(Vehicle)
admin.site.register(Order)
admin.site.register(Messages)
