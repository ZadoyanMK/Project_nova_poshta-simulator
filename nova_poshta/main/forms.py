from django import forms
from .models import Order, Vehicle
# from django.contrib.auth.models import


def choose_vehicle(weight, punkt_to, punkt_from):
    vehicles = Vehicle.objects.filter(
        punkt_to=punkt_to,
        punkt_where_staying=punkt_from
    ).order_by('-time_leaving')

    for veh in vehicles:
        if veh.max_weight > weight:
            Vehicle.objects.filter(
                name=veh.name
            ).update(max_weight=veh.max_weight - weight)
            return veh

    return Vehicle.objects.first()


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
        order.vehicle = choose_vehicle(order.weight, order.punkt_to, order.punkt_from)
        order.sender = request.user
        if commit:
            order.save()
        return order
