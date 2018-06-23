from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import *
from .forms import OrderModelForm, UserModelForm
from django.views.generic import TemplateView, View, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# Create your views here.


class UserCreateView(CreateView):
    form_class = UserModelForm
    template_name = 'app_sending_items/index.html'
    # success_url = 'add/user'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class OrderFormView(FormView):
    template_name = 'app_sending_items/index.html'
    form_class = OrderModelForm
    success_url = '/orders/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
