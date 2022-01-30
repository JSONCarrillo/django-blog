from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from blogApp.urls import index
from .forms import SignUpForm
from django.contrib.auth.views import PasswordChangeView

class userRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    # form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')
    fields = ['username', 'first_name', 'last_name', 'email']

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')

    def logout(request):
        logout(request)
        return redirect('login')