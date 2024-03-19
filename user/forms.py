from django import forms


class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)