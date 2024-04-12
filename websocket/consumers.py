import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from websocket.models import *

class ChatConsumer(AsyncWebsocketConsumer):
     async def connect(self):
        self.send_name = f"room_{self.scope['url_route']['kwargs']['send_name']}"
        self.receiver_username = f"room_{self.scope['url_route']['kwargs']['receiver_username']}"

        await self.channel_layer.group_add( self.send_name,self.receiver_username , self.channel_name)
        await self.accept()

    
     async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.send_name,self.receiver_username, self.channel_name)    