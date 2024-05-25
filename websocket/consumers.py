import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from websocket.models import *
from cryptography.fernet import Fernet
from django.conf import settings

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
        message = text_data_json
        print(message)

        event = {
            'type':'send_message', #aqui devemos digitar o nome da função que self.channel_layer.group_send ira
            'message': message,
        }
        await self.channel_layer.group_send(self.room_name, event) # envia os dados para todo mundo que esta conectao na url

     async def send_message(self, event):
         data = event['message']
         await self.create_message(data=data)
         response_data = {
            'sender': data['sender'],
            'message': data['message']
         }
         await self.send(text_data=json.dumps({'message': response_data}))    

     @database_sync_to_async #criamos essa função pois não é possivel manipular banco de dados dentro de uma função async
     def create_message(self, data):
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        message_original = data['message']
        message_bytes = message_original.encode('utf-8')
        message_encrypted = f.encrypt((message_bytes))
        message_decoded = message_encrypted.decode('utf-8')


        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(room=get_room_by_name, sender=data['sender'], message=message_decoded)
            new_message.save()