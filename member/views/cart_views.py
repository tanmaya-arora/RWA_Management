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
def add_to_cart(request):
    body = request.body
    data_str = body.decode('utf-8')
    # data_dict = json.loads(data_str)

    print("Body in add_to_cart API ",body)
    # for items in data_dict:
    #     # data = json.loads(items)
    #     print(items)
    #     user = User.objects.filter(email=items['user']).first()
    #     package = items.get('package')

    #     try:
    #         total_price = float(items.get('total_price'))
    #     except:
    #         total_price = 0.00
        
    #     # serializer = UserSerializer(user, many=False)

    #     try:
        
    #         cart_item = Cart.objects.create(
    #             package = package,
    #             user = user,
    #             total_price = total_price
    #         )

    #         cart_item.save()
    #     except Exception as e:
    #         return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return JsonResponse({"message": data_str}, status=status.HTTP_200_OK)
