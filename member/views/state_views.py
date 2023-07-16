from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import State
from member.serializers import StateSerializer


@api_view(['GET'])
def get_all_states(request):
    state = State.objects.all()
    serializer = StateSerializer(state, many=True)
    return Response(serializer.data)