import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from member.models import Cart
from member.serializers import UserSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def cart_details(request):
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