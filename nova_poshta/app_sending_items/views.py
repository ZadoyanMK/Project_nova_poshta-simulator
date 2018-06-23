from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import TemplateView, View, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# Create your views here.


# class