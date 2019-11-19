from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from shopify_auth.decorators import login_required
# Create your views here.

import requests
import json



def home(request, *args, **kwargs):
    return render(request, 'home.html')

def install(request):
    return render(request, 'home.html')

