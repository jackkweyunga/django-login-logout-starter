from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dashboard.mixins import LoginRequired
from .models import User
from .forms import UserForm

# CRUD
# Form Views


class UserCreateView(LoginRequired, generic.CreateView):
    model = User
    fields = [
        "email",
        "username",
        "password"
    ]
    
    
class UsersListView(LoginRequired, generic.ListView):
    model = User
    
    
class UserDetailView(LoginRequired, generic.detail.DetailView):
    model = User
    

class UserUpdateView(LoginRequired, generic.edit.UpdateView):
    model = User
    fields = [
        "email",
        "username",
        "first_name",
        "last_name"
    ]
    
    context_object_name = "selected_user"
    
    success_url = reverse_lazy('users:user-list')
    
    template_name = "users/user_update.html"
    
    def form_valid(self, form):
        return super().form_valid(form)

    
class UserDeleteView(generic.edit.DeleteView):
    model = User
    success_url = reverse_lazy('users:user-list')


class UserFormView(generic.edit.FormView):
    form_class = UserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy('users:user-list')

