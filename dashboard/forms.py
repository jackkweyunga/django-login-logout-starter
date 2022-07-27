from django import forms
from users.models import User

class UserCreationUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("email","password")


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

