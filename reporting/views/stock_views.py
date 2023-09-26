from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from reporting.models import ProductStock, SaleHistory
from internal.serializers import StockSerializer, SaleHistorySerializer, OrderSerializer
from internal.models import Order


@api_view(['GET'])
def get_all (request):
    stock = ProductStock.objects.all()
    serializer = StockSerializer(stock, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_stock_name (request, pk):
    try:
        stock = ProductStock.objects.filter(name =pk)
        serializer = StockSerializer(stock, many = False)
        return Response({'message':'Stock for the asked product'}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_order(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many= True)
    return Response(serializer.data)

    