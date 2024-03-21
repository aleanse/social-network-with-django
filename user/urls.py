from django.urls import path, include
from user import views



urlpatterns = [
    path('',views.register, name="register"),
    path('create-register', views.create_register, name="create-register")
]