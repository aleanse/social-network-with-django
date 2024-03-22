from typing import Any
from django import forms
from user.models import User
from django.core.exceptions import ValidationError
from django.http import Http404

class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password'}))

    class Meta: # especifica o modelo e os campos do modelo que serão usados
        model = User
        fields = ['username','email','password']

    def clean_username(self):
        data = self.cleaned_data.get('username')
        user = User.objects.filter(username=data).exists()
        if user:
            raise Http404('username already exists')
        else:
            return data
               
    def clean_email(self):
        data = self.cleaned_data.get('email')
        user = User.objects.filter(email=data).exists()
        if user:
            raise Http404('email already exists')
        else:
            return data
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise Http404('different passwords')