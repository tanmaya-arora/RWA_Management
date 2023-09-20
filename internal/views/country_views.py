from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from internal.models import Country
from internal.serializers import CountrySerializer


@api_view(['GET'])
def get_all_countries(request):
    country = Country.objects.all()
    serializer = CountrySerializer(country, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_country_by_id(request, pk):
    try:
        country = Country.objects.get(country_id = pk)
        serializer = CountrySerializer(country, many=False)
        message = {'Info': 'Country details fetched successfully', 'data': serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)