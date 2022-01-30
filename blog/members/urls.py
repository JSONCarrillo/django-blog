from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', userRegisterView.as_view(), name='register'),
    path('profile/edit-profile', UserEditView.as_view(), name='edit-profile'),
    path('change-password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='change-pass' )
    
]