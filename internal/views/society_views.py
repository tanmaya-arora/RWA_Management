from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from internal.models import Society
from internal.serializers import SocietySerializer


@api_view(['GET'])
def get_all_societies(request):
    society = Society.objects.all()
    serializer = SocietySerializer(society, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_society_by_id(request, pk):
    try:
        society = Society.objects.get(area_id = pk)
        serializer = SocietySerializer(society, many=False)
        message = {'Info': 'Area details fetched successfully', 'data': serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)