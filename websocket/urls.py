from django.urls import path
from websocket import views






urlpatterns = [
    path('create_room/', views.CreateRoom, name='room'),
    path('<int:id_unico>/', views.MessageView, name='message'),
    
]
