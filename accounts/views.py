from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

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
    form_class = SignUpForm # username, pass1, pass2
    success_url = reverse_lazy("login")
    
class CustomPasswordChangeView(PasswordChangeView):
    template_name = "accountsTemplates/change_password.html"
    success_url = reverse_lazy("change_password_done")
    
class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "accountsTemplates/change_password_done.html"
    

# First: User enters email to get the reset link
class CustomPasswordResetView(PasswordResetView):
    template_name = "accountsTemplates/password_reset.html" # Display form and button
    email_template_name = "accountsTemplates/password_reset_email.html" # Modify content of the email
    subject_template_name = "accountsTemplates/password_reset_subject.txt" # Modify the Subject of the email
    
# Second: Just a template to let know to the user that an email has been sent 
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accountsTemplates/password_reset_done.html"
    
# Third: Display the reset form IF user clicked on the secure link from th eemail
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accountsTemplates/password_reset_confirm.html"

# Fourth: Display a successful message and tell the user to try and login again
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accountsTemplates/password_reset_complete.html"
    
