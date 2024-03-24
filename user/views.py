from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from user.utils.authenticate import authenticate_by_email
from django.contrib import messages

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
    



def login_view(request):
    form = LoginForm()
    return render(request,'login.html',context={'form':form})




def create_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate_by_email(form.cleaned_data.get('email',''),
                                     form.cleaned_data.get('password'))

        if user is not None:
            login(request,user)
            messages.success(request,'login feito com sucesso')
            return redirect('home')

        elif user is None:
            messages.error(request,'Invalid credentials')

    return redirect('login')


def logout_view(request):
    logout(request)
    messages.success(request,'logout feito com sucesso')
    return redirect('home')


def home(request):
    return render(request, 'home.html')

