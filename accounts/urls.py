from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView, 
    SignUpView, 
    CustomPasswordChangeView, 
    CustomPasswordChangeDoneView,
    CustomPasswordResetCompleteView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetDoneView,
    CustomPasswordResetView
)

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name= "login"),
    path("logout/", CustomLogoutView.as_view(), name= "logout"),
    path("signup/", SignUpView.as_view(), name= "signup"),
    path("change_password/", CustomPasswordChangeView.as_view(), name= "change_password"),
    path("change_password_done/", CustomPasswordChangeDoneView.as_view(), name= "change_password_done"),
    path("password_reset/", CustomPasswordResetView.as_view(), name= "password_reset"),
    path("password_reset/done/", CustomPasswordResetDoneView.as_view(), name= "password_reset_done"),
    path("reset/<uidb64>/<token>", CustomPasswordResetConfirmView.as_view(), name= "password_reset_confirm"),
    # http://localhost:8000/accounts/reset/MQ/
    path("reset/done/", CustomPasswordResetCompleteView.as_view(), name= "password_reset_complete"),

]