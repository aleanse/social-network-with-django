from django.http import JsonResponse
from django.shortcuts import redirect, render
from user.models import User
from .models import Message,Room
import uuid

id_unico = uuid.uuid4()


def CreateRoom(request):
    receiver_username = id_unico
    room = request.user.username
    try:
        return redirect('message', room_name=room, receiver_username=receiver_username)
    except Room.DoesNotExist:
        new_room = Room(room_name=room)
        new_room.save()
        return redirect('message', room_name=room, receiver_username=receiver_username)


def MessageView(request,room_name,receiver_username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)
    

    return render(request, 'messages.html',context={"messages": get_messages,
        "receiver_username": receiver_username,
        "room_name": room_name,})



