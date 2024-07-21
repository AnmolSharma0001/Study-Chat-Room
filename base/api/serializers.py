from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializeer(ModelSerializer):
    class Meta:
        model = Room
        fields  = '__all__'

# to turn to json data from python query
