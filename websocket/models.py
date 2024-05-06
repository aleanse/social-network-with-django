from django.db import models
from user.models import User
import  django.utils.timezone

    
class Room(models.Model):
    room_name = models.CharField(max_length=255)
    sender_name = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sent_messages',default=False)
    receiver_name = models.ForeignKey(User, on_delete=models.CASCADE,related_name='received_messages',default=False )

    def __str__(self):
        return self.room_name
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,default=True)
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