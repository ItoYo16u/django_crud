from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm,LogInForm
from django.contrib.auth.views import LoginView

# Create your views here.

class SignUp(generic.CreateView):
    form_class=SignUpForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

class LogIn(LoginView):
    form_class=LogInForm
    template_name='accounts/login.html'