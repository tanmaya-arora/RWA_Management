from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from internal.models import City
from internal.serializers import CitySerializer


@api_view(['GET'])
def get_all_cities(request):
    city = City.objects.all()
    serializer = CitySerializer(city, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_city_by_id(request, pk):
    try:
        city = City.objects.get(city_id = pk)
        serializer = CitySerializer(city, many=False)
        message = {'Info': 'City details fetched successfully', 'data': serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)