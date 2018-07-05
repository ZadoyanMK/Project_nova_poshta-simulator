from __future__ import absolute_import, unicode_literals

from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import login, logout


from .forms import OrderModelForm
from .models import *
from .tasks import *


# Create your views here.
def to_main(request):
    return HttpResponseRedirect(reverse_lazy('form-main'))


class MainFormView(TemplateView):
    template_name = 'main/main.html'

    def get(self, request):
        if request.user.is_authenticated:
            orders_searching = Order.objects.filter(sender=request.user, status=Order.STATUS_SEARCHING_FOR_TRANSPORT)
            orders_waiting = Order.objects.filter(sender=request.user, status=Order.STATUS_WAITING_FOR_TRANSPORTING)
            orders_sending = Order.objects.filter(sender=request.user, status=Order.STATUS_SENDING)
            orders_finished = Order.objects.filter(sender=request.user, status=Order.STATUS_SENDED)
            messages = Messages.objects.filter(user=request.user)
            ctx = {}

            ctx['orders_waiting'] = orders_waiting
            ctx['orders_sending'] = orders_sending
            ctx['orders_finished'] = orders_finished
            ctx['orders_searching'] = orders_searching
            ctx['messages'] = messages
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class OrderFormView(FormView):
    template_name = 'main/order.html'
    form_class = OrderModelForm
    success_url = reverse_lazy('form-main')

    def get(self, request, *args, **kwargs):
        orders_searching = Order.objects.filter(sender=request.user, status=Order.STATUS_SEARCHING_FOR_TRANSPORT)
        orders_waiting = Order.objects.filter(sender=request.user, status=Order.STATUS_WAITING_FOR_TRANSPORTING)
        orders_sending = Order.objects.filter(sender=request.user, status=Order.STATUS_SENDING)
        orders_finished = Order.objects.filter(sender=request.user, status=Order.STATUS_SENDED)
        messages = Messages.objects.filter(user=request.user)
        ctx = {}

        ctx['orders_waiting'] = orders_waiting
        ctx['orders_sending'] = orders_sending
        ctx['orders_finished'] = orders_finished
        ctx['orders_searching'] = orders_searching
        ctx['messages'] = messages
        ctx['form'] = self.form_class
        return render(request, self.template_name, ctx)

    def form_valid(self, form):
        form.save(self.request)
        return HttpResponseRedirect(self.success_url)
