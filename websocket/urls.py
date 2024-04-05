from django.urls import path
from websocket import views


urlpatterns = [
    path('messages/', views.CreateRoom, name='create-room'),
    path('<int:send_name>/<int:receiver_username>/', views.MessageView, name='room'),
    
]
