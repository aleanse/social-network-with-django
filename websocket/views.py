from django.shortcuts import render
from user.models import User
from .models import Message
# Create your views here.

#def CreateRoom(request):
 #   if request.method == 'POST':
  #       user = request.user
   #      sent_messages = Message.objects.filter(sender=user)
    #     data = [{'sender': message.sender.username, 'receiver': message.receiver.username, 'content': message.content, 'timestamp': message.timestamp} for message in sent_messages]
     #    return JsonResponse(data, safe=False)
    #return render(request, 'index.html')


def MessageView(request, send_name, receiver_username):
    sender = request.user
    receiver = User.objects.get(id=receiver_username)
    try:
        message = Message.objects.get_or_create(sender=sender,receiver=receiver)
        print(message)    
    except message.DoesNotExist:
        message = Message(sender=sender,receiver=receiver)
        message.save()    
    return render(request, 'messages.html',context={'messages':message,
                                                    'sender':sender,
                                                    'receiver':receiver})



