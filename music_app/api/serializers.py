from rest_framework.serializers import ModelSerializer
from .models import Room


# Create your serialisers here.

class RoomSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Room
