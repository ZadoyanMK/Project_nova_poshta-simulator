from django.contrib import admin
from .models import User, Punkt, Vehicle
# Register your models here.

admin.site.register(User)
admin.site.register(Punkt)
admin.site.register(Vehicle)
