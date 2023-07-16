from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Country
from member.serializers import CountrySerializer


@api_view(['GET'])
def get_all_countries(request):
    country = Country.objects.all()
    serializer = CountrySerializer(country, many=True)
    return Response(serializer.data)