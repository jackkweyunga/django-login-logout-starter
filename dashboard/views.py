from django.shortcuts import render, redirect

from users.models import User
from .mixins import LoginRequired
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# django
from django.views import View

class IndexView(LoginRequired, View):
    
    """ Index View """  
    
    def get(self, request):
        
        context = {
            "user":request.user
        }
        
        return render(request, "dashboard/index.html", context=context)
