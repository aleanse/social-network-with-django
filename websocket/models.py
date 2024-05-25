from django.db import models
from user.models import User
import  django.utils.timezone
from cryptography.fernet import Fernet
from django.conf import settings


    
class Room(models.Model):
    room_name = models.UUIDField(primary_key=True, editable=False)
    users = models.ManyToManyField(User, related_name='chat_rooms')
    def __str__(self):
        return str(self.room_name)
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    @property
    def message_decrypted(self):
        f = Fernet(settings.ENCRYPT_KEY)
        message_decrypted = f.decrypt(self.message)
        message_decode = message_decrypted.decode('utf-8')

        return message_decode

    def __str__(self):
        return str(self.room)
   