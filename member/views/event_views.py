import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from member.models import Event
from member.serializers import EventSerializer


@api_view(['GET'])
def get_events(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)
    message = {'Info': 'All Events fetched successfully', 'data': serializer.data}
    return Response(message, status=status.HTTP_200_OK)