from django.db import models
from user.models import User
import  django.utils.timezone
import uuid


    
class Room(models.Model):
    room_name = models.UUIDField(primary_key=True, editable=False)
    users = models.ManyToManyField(User, related_name='chat_rooms')
    def __str__(self):
        return str(self.room_name)
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return str(self.room)
   # sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    #receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    #content = models.TextField()
    #timestamp = models.DateTimeField(auto_now_add=True)
    #def __str__(self):
    #   return f"From: {self.sender} - To: {self.receiver} - {self.timestamp}"