from django.forms import ModelForm
from .models import User

# User Creation Form

class UserForm(ModelForm):
    
    class Meta:
        model = User
        
        fields = [
            "email",
            "password",
            "first_name",
            "last_name"
        ]
        
        