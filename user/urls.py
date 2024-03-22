from django.urls import path, include
from user import views



urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('create-register/', views.create_register, name="create-register"),
    path('login/', views.login, name="login"),
    path('login/create-login/', views.create_login, name="create-login")
]