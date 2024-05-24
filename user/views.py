from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm, PostForm, Edit_profileForm
from django.contrib.auth import  login, logout
from user.utils.authenticate import authenticate_by_email
from django.contrib import messages
from user.models import User, Seguidor


# Create your views here.

def register(request):
    form = RegisterForm()
    return render(request,'register.html',context={'form':form})

def create_register(request):
    form = RegisterForm(request.POST, request.FILES)
    if form.is_valid():
        user = form.save(commit=False) #salva os dados mas ainda não manda para o banco de dados
        user.set_password(user.password)
        if 'image' in request.FILES:
                user.photo = request.FILES['image']
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html', {'form': form})
    
def login_view(request):
    print('ola')
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


def post(request):
    form = PostForm()
    return render(request,'create_post.html',context={'form':form})

def create_post(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
    else:
        print(form.errors)
    return redirect('home')


@login_required(login_url='register', redirect_field_name='next')
def logout_view(request):
    if request.GET:
        return redirect('login')

    logout(request)
    messages.success(request,'logout feito com sucesso')
    return redirect('home')

def profile(request):
    user = request.user
    
    return render(request, 'profile.html',context={'user':user})




def users(request):
    user = User.objects.all()
    return render(request,'users1.html',context={'user':user})


@login_required(login_url='register', redirect_field_name='next')
def follow(request,id):
    usuario_a_seguir = User.objects.get(id=id)
    seguido = Seguidor.objects.get_or_create(usuario=request.user, seguindo=usuario_a_seguir)
    return redirect('users')


@login_required(login_url='register', redirect_field_name='next')
def edit_profile(request):
    form = Edit_profileForm()
    return render(request,'edit_profile.html',context={'form':form})


def create_edit_profile(request):
    instance_user = request.user
    form = Edit_profileForm(request.POST,request.FILES,instance=instance_user)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        if 'image' in request.FILES:
                user.photo = request.FILES['image']
        user.save()
    else:
        print(form.errors)
    return redirect('home')

def area_user(request, id):
    user = User.objects.get(id=id)
    seguido = Seguidor.objects.get_or_create(usuario=request.user, seguindo=user)
    return render(request,'area_profile.html',context={'user':user})


def home(request):
    users = User.objects.all()
    return render(request, 'home.html',context={'users':users})

