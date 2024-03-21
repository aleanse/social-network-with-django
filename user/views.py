from django.shortcuts import render
from user.forms import RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm()
    return render(request,'register.html',context={'form':form})

def create_register(request):
    form = RegisterForm(request.POST)
    return 'ola mundo'
