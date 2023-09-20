from rest_framework.decorators import api_view
from rest_framework.response import Response
from internal.models import Package, Package_Category
from rest_framework import status
from internal.serializers import PackageSerializer, PackageCategoriesSerializer
import json


@api_view(['GET'])
def get_package_categories(request):
    package_categories = Package_Category.objects.all()
    Serializer = PackageCategoriesSerializer(package_categories,many=True)
    return Response(Serializer.data)

@api_view(['GET'])
def get_package(request,pk):
    try:
        categories = Package_Category.objects.get(_id = pk)
        serializer = PackageCategoriesSerializer(categories, many = False)
        message = {'Info':'package details fetched successfully','data':serializer.data}
        return Response(message,status=status.HTTP_200_OK)

    except:
        message = {'error':'category not found'}
        return Response(message,status=status.HTTP_303_SEE_OTHER)   
        
@api_view(['POST'])
def get_package_categories_by_user_type(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    package_obj = Package.objects.all()
    slz = PackageSerializer(package_obj, many=True)
    package = slz.data
    
    userValue = 1
    for items in package:
        if items["name"] == data_dict['user_type']:
            userValue = items["_id"]

    pcg = Package_Category.objects.filter(category = userValue)

    serializer = PackageCategoriesSerializer(pcg, many = True)
    message = {'Info': 'Package categories successfully fetched', 'data': serializer.data}
    return Response(message, status=status.HTTP_200_OK)
