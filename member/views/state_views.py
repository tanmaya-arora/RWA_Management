from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from member.models import State
from member.serializers import StateSerializer


@api_view(['GET'])
def get_all_states(request):
    state = State.objects.all()
    serializer = StateSerializer(state, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_state_by_id(request, pk):
    try:
        state = State.objects.get(state_id = pk)
        serializer = StateSerializer(state, many=False)
        message = {'Info': 'State details fetched successfully', 'data': serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)