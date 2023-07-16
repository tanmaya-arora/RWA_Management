from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import City
from member.serializers import CitySerializer


@api_view(['GET'])
def get_all_cities(request):
    city = City.objects.all()
    serializer = CitySerializer(city, many=True)
    return Response(serializer.data)