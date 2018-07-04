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


# Create your views here.
def to_main(request):
    return HttpResponseRedirect(reverse_lazy('form-main'))


class MainFormView(TemplateView):
    template_name = 'main/main.html'

    def get(self, request):
        if request.user.is_authenticated:
            orders_current = Order.objects.filter(sender=request.user, completed=False)
            orders_finished = Order.objects.filter(sender=request.user, completed=True)
            messages = Messages.objects.filter(user=request.user)
            ctx = {}
            ctx['orders_current'] = orders_current
            ctx['orders_finished'] = orders_finished
            ctx['messages'] = messages
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class OrderFormView(FormView):
    template_name = 'main/order.html'
    form_class = OrderModelForm
    success_url = reverse_lazy('form-main')

    def get(self, request, *args, **kwargs):
        orders_current = Order.objects.filter(sender=request.user, completed=False)
        orders_finished = Order.objects.filter(sender=request.user, completed=True)
        form = self.form_class
        ctx = {}
        ctx['orders_current'] = orders_current
        ctx['orders_finished'] = orders_finished
        ctx['form'] = form
        return render(request, self.template_name, ctx)

    def form_valid(self, form):
        form.save(self.request)
        return HttpResponseRedirect(self.success_url)
