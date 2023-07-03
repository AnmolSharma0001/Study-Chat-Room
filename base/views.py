from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.

# def home(request):
#     return HttpResponse('home page')

# def room(request):
#     return HttpResponse('room page')

# rooms = [
#     {'id': 1, 'name': 'new1'},
#     {'id': 2, 'name': 'new2'},
#     {'id': 3, 'name': 'new3'}
# ]


def home(request):
    rooms=Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {'room' : room}
    return render(request, 'room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')

    context={'form' : form}
    return render(request, "room_form.html", context)