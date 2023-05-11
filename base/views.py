from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse('home page')

# def room(request):
#     return HttpResponse('room page')

rooms = [
    {'id': 1, 'name': 'new1'},
    {'id': 2, 'name': 'new2'},
    {'id': 3, 'name': 'new3'}
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if int(pk) == i['id']:
            room = i
    context = {'room' : room}
    return render(request, 'room.html', context)
