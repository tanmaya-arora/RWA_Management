# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Package_attributes
import json

@api_view(['POST'])
def create_attributes(request):
    try:
        data = json.loads(request.body)
        package_details = data.get('package_details')
        name = data.get('name')
        price = data.get('price', 0)
        status = data.get('status')
        no_of_days = data.get('no_of_days')

        if not all([package_details, name, status, no_of_days]):
            return Response({'error': 'Missing required fields.'}, status=400)

        updated_items = Package_attributes.objects.create(
            package_details=package_details,
            name=name,
            price=price,
            status=status,
            no_of_days=no_of_days,
        )
        updated_items.save()
        return Response({'message': 'Attributes Added Successfully'}, status=201)
    except :
        return Response({'message':'Attributes Already Exist'} )
