from django import forms
from .models import Order, Vehicle
from django.contrib.auth.models import User

# from django.contrib.auth.models import

from .tasks import message_creating, message_creating_with_new_user


def choose_vehicle(weight, punkt_to, punkt_from):
    vehicles = Vehicle.objects.filter(
        punkt_to=punkt_to,
        punkt_where_staying=punkt_from
    ).order_by('-time_leaving')

    for veh in vehicles:
        if veh.max_weight > weight + veh.total_weight and veh.status == Vehicle.STATUS_STOPPED:
            Vehicle.objects.filter(
                id=veh.id
            ).update(total_weight=veh.total_weight + weight)
            return veh

    return None


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
        if order.vehicle is not None:
            order.status = Order.STATUS_WAITING_FOR_TRANSPORTING
        else:
            order.status = Order.STATUS_SEARCHING_FOR_TRANSPORT

        getter = User.objects.filter(
            first_name=order.getter_name,
            last_name=order.getter_surname,
            email=order.getter_email,
        ).first()

        if getter is not None:
            message_creating.delay(request.user.id, getter.id, order.order_name)
        else:
            new_user = User.objects.create_user(
                username=order.getter_name + '.' + order.getter_surname,
                first_name=order.getter_name,
                last_name=order.getter_surname,
                email=order.getter_email,
                password='123'
            )
            message_creating_with_new_user(request.user.id, new_user.id, order.order_name)
        if commit:
            order.save()
        return order
