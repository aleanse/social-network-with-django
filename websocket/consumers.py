import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from websocket.models import *
from cryptography.fernet import Fernet
from django.conf import settings
import uuid

f = Fernet(settings.ENCRYPT_KEY)

class ChatConsumer(AsyncWebsocketConsumer):
     async def connect(self):
        self.room_name = (f"room_{self.scope['url_route']['kwargs']['room_name']}")
        await self.channel_layer.group_add(self.room_name, self.channel_name) #adiciona o usuario que esta url self.room_name ao canal websocket
        await self.accept()

    
     async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

     async def receive(self, text_data):    #recebe os dados de quem ja esta conectado na url
        text_data_json = json.loads(text_data)
        message_id = text_data_json.get('message_id', str(uuid.uuid4()))
        message = text_data_json
        sender = message['sender']
        receive = message['receive']
        room_name = text_data_json.get('room_name')
        user = self.scope['user']
        data = {
            'message_id': message_id,
            'message': message,
            'room_name': room_name,
            'sender': sender,
            'receive': receive
        }
        event = {
            'type': 'send_message',
            'message': data,
        }
        await self.channel_layer.group_send(self.room_name, event)

     async def send_message(self, event):
         data = event['message']
         print(data)
         await self.create_message(data=data)


         response_data = {
            'sender': data['sender'],
            'message': data['message']
         }
         await self.send(text_data=json.dumps({'message': response_data}))    

     @database_sync_to_async #criamos essa função pois não é possivel manipular banco de dados dentro de uma função async
     def create_message(self, data):
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        message_id = data['message_id']

        if not Message.objects.filter(message_id=message_id).exists():
            message_original = data['message']['message']
            message_bytes = message_original.encode('utf-8')
            message_encrypted = f.encrypt((message_bytes))
            message_decoded = message_encrypted.decode('utf-8')
            new_message = Message(
              room=get_room_by_name,
              sender=data['sender'],
              message=message_decoded,
              message_id=message_id
             )
            new_message.save()