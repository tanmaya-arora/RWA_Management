import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from member.models import Cart
from member.serializers import CartSerializer, UserSerializer
from django.contrib.auth.models import User


@api_view('GET')
def get_cart_items(request):
    cart = Cart.objects.all()
    serializer = CartSerializer(cart, many=True)
    message = {'Info': 'Cart items fetched successfully', 'data': serializer.data}
    return Response(message, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_to_cart(request):
    data = json.loads(request.body)
    user = User.objects.filter(email=data['user']).first()

    serializer = UserSerializer(user, many=False)

    # package = data.get('package')
    # total_price = data.get('total_price', 0)

    # cart_item = Cart.objects.create(
    #         package =package,
    #         user=user,
    #         total_price=total_price
    #     )
    
    # cart_item.save()

    return JsonResponse({'message': serializer.data})