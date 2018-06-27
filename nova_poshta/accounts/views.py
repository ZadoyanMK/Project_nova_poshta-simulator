# from django.views.generic import TemplateView, View, ListView, DetailView
# from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm

from django.core.mail import send_mail
from .tasks import *
# from .forms import OrderModelForm
# from .models import *


# Create your views here.


class UserCreateView(FormView):
    template_name = 'accounts/index.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('form-main')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class UserLoginView(FormView):
    template_name = 'accounts/index.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('form-main')

    def form_valid(self, form):
        login(self.request, form.get_user())
        # SignUp.delay(self.request.user)
        # add.delay(1, 2)
        return HttpResponseRedirect(self.success_url)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('form-main'))
