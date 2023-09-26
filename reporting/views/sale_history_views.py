from rest_framework import generics
from reporting.models import SaleHistory
from internal.models import Order
from internal.serializers import SaleHistorySerializer, OrderSerializer
from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
class SaleHistoryCreateView(generics.CreateAPIView):
    queryset = SaleHistory.objects.all()
    serializer_class = SaleHistorySerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# @api_view(['GET'])
# def SaleHistory(request):
#     history = SaleHistory.objects.all()
#     serializer = SaleHistorySerializer(history, many = True)
#     return Response(serializer.data)
    