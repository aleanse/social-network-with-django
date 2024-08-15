from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.deprecation import MiddlewareMixin

from user.forms import RegisterForm, LoginForm, PostForm, Edit_profileForm
from django.contrib.auth import  login, logout
from user.utils.authenticate import authenticate_by_email
from django.contrib import messages
from user.models import User, Seguidor, Post,Like, Comment


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
    next_url = request.GET.get('next')
    if next_url:
        messages.info(request, 'Você precisa realizar login antes de realizar essa ação.')
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

    return render(request,'users.html',context={'user':user})


@login_required(login_url='register', redirect_field_name='next')
def follow(request,id):
    usuario_a_seguir = User.objects.get(id=id)
    seguido = Seguidor.objects.get_or_create(usuario=request.user, seguindo=usuario_a_seguir)
    return redirect('users')


@login_required(login_url='register', redirect_field_name='next')
def unfollow(request,id):
    usuario_a_seguir = User.objects.get(id=id)
    seguido = Seguidor.objects.get(usuario=request.user, seguindo=usuario_a_seguir)
    if seguido:
        seguido.delete()    
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
    return render(request,'area_profile.html',context={'i':user})

@login_required(login_url='login', redirect_field_name='next')
def like(request, id):
    post = get_object_or_404(Post,id=id)
    like = Like.objects.create(user=request.user, post=post)
    return redirect('home')
    
@login_required(login_url='login', redirect_field_name='next')
def deslike(request, id):
    post = get_object_or_404(Post,id=id)
    like = Like.objects.get(user=request.user, post=post)
    like.delete()
    
    return redirect('home')    


def home(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'home.html',context={'posts': posts })


@login_required(login_url='login', redirect_field_name='next')
def make_comment(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        text = request.POST.get('user_input')
        if text:
            comment = Comment.objects.create(text=text,author= request.user,post=post)
            comments = post.comments.all()
            return redirect('home')
    return redirect('home')

@login_required(login_url='login', redirect_field_name='next')
def comment(request, id):
    post = Post.objects.get(id=id)
    comments = post.comments.all().order_by('-created_at')
    return render(request, 'comments.html',context={'comments':comments})


