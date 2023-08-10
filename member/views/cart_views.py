# views.py
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from member.models import Cart

from member.serializers import CartSerializer, UserSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def get_cart_items(request):
    cart = Cart.objects.all()
    serializer = CartSerializer(cart, many=True)
    message = {'Info': 'Cart items fetched successfully', 'data': serializer.data}
    return Response(message, status=status.HTTP_200_OK)

@api_view(['POST'])
def cart_details(request):
    body = request.body
    data_str = body.decode('utf-8')
    data_dict = json.loads(data_str)
    # data = json.loads(request.body)
    
    for items in data_dict:
        # data = json.loads(items)
        print(items)
        user = User.objects.filter(email=items['user']).first()
        package = items.get('package')
        quantity = items.get('quantity')
        total_price = items.get('total_price')

        cart_item = Cart.objects.create(
            package = package,
            quantity = quantity,
            total_price = total_price,
            user = user
        )

        #cart_item.quantity += quantity
        cart_item.save()

    return JsonResponse({'message': 'Items added to cart successfully.'}, status=status.HTTP_200_OK)
