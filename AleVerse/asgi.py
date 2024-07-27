import os

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

# imports
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from websocket import routing
from websocket.consumers import ChatConsumer
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AleVerse.settings')



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns  # Substitua 'routing.websocket_urlpatterns' com o seu roteamento de WebSocket
            )
        )
    ),
})


