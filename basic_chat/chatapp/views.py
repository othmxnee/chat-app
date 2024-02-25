from django.shortcuts import render
import threading
from .models import ChatMessage

def index(request):
    print(threading.get_native_id())
    return render(request, 'chatapp/index.html')

def room(request, room_name):
    # Fetch the last 50 messages (or however many you prefer) in this room
    # Adjust the ordering and limit as necessary
    messages = ChatMessage.objects.filter(room_name=room_name).order_by('-id')[:50]

    return render(request, 'chatapp/room.html', {
        'room_name': room_name,
        'messages': messages,
    })