from django.urls import path
from websocket import views






urlpatterns = [
    path('create_room/<int:id_receiver>/', views.CreateRoom, name='room'),
    path('<str:room_name>/<str:username>/', views.MessageView, name='message'),
    
]
