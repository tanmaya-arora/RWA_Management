# views.py
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from internal.models import Cart

from internal.serializers import CartSerializer, UserSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def get_cart_items(request):
    cart = Cart.objects.all()
    serializer = CartSerializer(cart, many=True)
    message = {'Info': 'Cart items fetched successfully', 'data': serializer.data}
    return Response(message, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_cart_items_by_user(request, pk):
    try:
        cart = Cart.objects.filter(user=pk)
        serializer = CartSerializer(cart, many=True)
        message = {'Info': 'Cart items fetched successfully', 'data': serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def cart_details(request):
    body = request.body
    data_str = body.decode('utf-8')
    data_dict = json.loads(data_str)
    
    for items in data_dict:
        user = User.objects.filter(email=items['user']).first()
        package = items.get('package')
        quantity = items.get('quantity')
        img_path = items.get('image_path')
        package_details = items.get('package_detail')
        total_price = items.get('total_price')

        cart_item = Cart.objects.create(
            package = package,
            quantity = quantity,
            package_details = package_details,
            image_path = img_path,
            total_price = total_price,
            user = user
        )
        cart_item.save()

    return JsonResponse({'message': 'Items added to cart successfully.'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def remove_items(request, id):
    try:
        item = Cart.objects.filter(id=id)
        item.delete()
        message = {'message':'Item removed successfully'}
        return Response(message, status=status.HTTP_200_OK)

    except Exception as e: 
        message = {'error':str(e)}
        return Response(message, status=status.HTTP_406_NOT_ACCEPTABLE)