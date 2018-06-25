from django import forms
from .models import Order, Vehicle
# from django.contrib.auth.models import


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'weight',
            'order_name',
            'getter_email',
            'getter_name',
            'getter_surname',
            'punkt_from',
            'punkt_to',
        ]

    def save(self, request, commit=True):
        order = super(OrderModelForm, self).save(commit=False)
        order.vehicle = Vehicle.objects.first()
        order.sender = request.user
        if commit:
            order.save()
        return order
