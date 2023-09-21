from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from reporting.models import ProductStock
from internal.serializers import StockSerializer


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
        return Response({'message':'Stock for the asked product'})
    