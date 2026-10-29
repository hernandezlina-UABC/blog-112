from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    # SigninView,
)
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class CustomLoginView(LoginView): # 
    # template_name attribute renders aspecific html
    template_name = "accountsTemplates/login.html"
    
class CustomLogoutView(LogoutView): # 
    # template_name attribute renders aspecific html
    template_name = "accountsTemplates/logout.html"
    
class SignUpView(CreateView): # 
    # template_name attribute renders aspecific html
    template_name = "accountsTemplates/signup.html"
    
    # form_class attribute allow us to create objects from a form file
    # we use this one when we want to have a custom form
    form_class = UserCreationForm # username, pass1, pass2
    success_url = reverse_lazy("login")