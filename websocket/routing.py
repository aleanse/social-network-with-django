from django.urls import re_path ,path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/notification/<str:room_name>/', ChatConsumer.as_asgi()),
]