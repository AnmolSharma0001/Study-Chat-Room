from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, Topic, Message
from .serializers import RoomSerializeer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]

    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = (Room.objects.all())
    serializer = RoomSerializeer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    rooms = Room.objects.filter(id=pk)
    serializer = RoomSerializeer(rooms, many=True)
    return Response(serializer.data)

# functions for api
