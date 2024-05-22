from django import forms
from user.models import User
from django.core.exceptions import ValidationError

class Edit_profileForm(forms.ModelForm):
    email = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Username'}),)
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password'}))

    

    class Meta: # especifica o modelo e os campos do modelo que serão usados
        model = User
        fields = ['username','email','password']

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise ValidationError({'password':'Passwords must be equal'})