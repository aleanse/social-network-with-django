from django.urls import path, include
from user import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register, name="register"),
    path('create-register/', views.create_register, name="create-register"),
    path('login/', views.login_view, name="login"),
    path('login/create-login/', views.create_login, name="create-login"),
    path('logout/', views.logout_view, name='logout'),
    path('post/',views.post,name='post'),
    path('post/create-post',views.create_post,name='create-post'),
    path('profile/',views.profile,name='profile'),
    path('users/',views.users,name='users'),
    path('users/<int:id>',views.follow,name='follow'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('create_edit_profile/',views.create_edit_profile,name='create_edit_profile'),
    path('user/<int:id>',views.area_user,name='area_user'),
    path('like/<int:id>',views.like,name='like'),
    path('deslike/<int:id>',views.deslike,name='deslike')


]

