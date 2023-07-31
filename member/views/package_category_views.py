from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Package_category
from rest_framework import status
from member.serializers import PackageCategoriesSerializer
import json


@api_view(['GET'])
def get_package_categories(request):
    package_categories = Package_category.objects.all()
    Serializer =PackageCategoriesSerializer(package_categories,many=True)
    return Response(Serializer.data)


@api_view(['POST'])
def get_package_categories_by_user_type(request):
    data = request.body

    data_str = data.decode('utf-8')

    data_dict = json.loads(data_str)

    userValue = data_dict['user_type']
    pcg = Package_category.objects.filter(package = userValue)

    serializer = PackageCategoriesSerializer(pcg, many = True)
    message = {'Info': 'Package categories successfully fetched', 'data': serializer.data}
    return Response(message, status=status.HTTP_200_OK)
