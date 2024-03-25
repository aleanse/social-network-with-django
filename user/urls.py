from django.urls import path, include
from user import views



urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('create-register/', views.create_register, name="create-register"),
    path('login/', views.login_view, name="login"),
    path('login/create-login/', views.create_login, name="create-login"),
    path('logout/', views.logout_view, name='logout'),
    path('post/',views.post,name='post'),
    path('post/create-post',views.create_post,name='create-post')
]