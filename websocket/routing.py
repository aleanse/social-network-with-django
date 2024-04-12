from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/notification/<int:send_name>/<int:receiver_username>', ChatConsumer.as_asgi()),
]