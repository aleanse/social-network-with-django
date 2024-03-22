from django import forms
from user.models import User
from django.http import Http404

class LoginForm(forms.Form):
    email = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    

    
                 