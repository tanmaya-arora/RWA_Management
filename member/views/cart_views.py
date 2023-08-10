# views.py
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from member.models import Cart

@api_view(['POST'])
def cart_details(request):
    data = json.loads(request.body)
    
    package = data.get('package')
    quantity = data.get('quantity', 1)
    total_price = data.get('total_price', 0)

    try:
        cart_item = Cart.objects.create(
            package = package,
            quantity = quantity,
            total_price = total_price
        )

        cart_item.quantity += quantity
        cart_item.save()

        return JsonResponse({'message': 'Item added to cart successfully.'})
    except:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)
