from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Package, Package_Category
from rest_framework import status
from member.serializers import PackageSerializer, PackageCategoriesSerializer
import json


@api_view(['GET'])
def get_package_categories(request):
    package_categories = Package_Category.objects.all()
    Serializer = PackageCategoriesSerializer(package_categories,many=True)
    return Response(Serializer.data)


@api_view(['POST'])
def get_package_categories_by_user_type(request):
    data = request.body

    data_str = data.decode('utf-8')

    data_dict = json.loads(data_str)

    package = Package.objects.all()
    slz = PackageSerializer(package, many=True)
    
    # userValue = data_dict['user_type']
    # pcg = Package_Category.objects.filter(package = userValue)

    # serializer = PackageCategoriesSerializer(pcg, many = True)
    message = {'Info': 'Package categories successfully fetched', 'data': slz.data}
    return Response(message, status=status.HTTP_200_OK)
