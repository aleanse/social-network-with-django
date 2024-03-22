from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from user.utils.authenticate import authenticate_by_email

# Create your views here.

def register(request):
    form = RegisterForm()
    return render(request,'register.html',context={'form':form})

def create_register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False) #salva os dados mas ainda não manda para o banco de dados
        user.set_password(user.password)
        user.save()
        return redirect('login')
    


def login(request):
    form = LoginForm()
    return render(request,'login.html',context={'form':form})


def create_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate_by_email(form.cleaned_data.get('email',''),
                                     form.cleaned_data.get('password'))
        if user is not None:
            login(request,user)
            return redirect('home')
        elif user is None:
            return redirect('register')  
        
def home(request):
    return render(request, 'home.html')

