from django.http import JsonResponse
from django.shortcuts import redirect, render
from user.models import User
from .models import Message, Room
import uuid
from django.db.models import Q
from cryptography.fernet import Fernet
from django.conf import settings



def CreateRoom(request, id_receiver):
    user = request.user
    receiver = User.objects.get(id=id_receiver)  # pega o usuario destinatario
    try:

        get_room = Room.objects.filter(users=user).filter(
            users=receiver).distinct().first()  # tenta pegar a sala onde onde estão ligados o destinatario e remetente
        if get_room == None:
            raise Room.DoesNotExist

        return redirect('message', room_name=str(get_room.room_name), username=user.username)
    except Room.DoesNotExist:
        room = Room.objects.create(room_name=uuid.uuid4())
        room.users.add(user, receiver)
        return redirect('message', room_name=str(room.room_name), username=user.username)


def MessageView(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)
    receive = get_room.users.exclude(id=request.user.id).first()
    user = request.user.username

    return render(request, 'messages.html', context={
        "messages": get_messages,
        "user": user,
        "room_name": room_name,
        "receive": receive
    })

