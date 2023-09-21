from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from support.models import Ticket
from internal.serializers import TicketSerializer
import json
from django.contrib.auth.models import User

@api_view(['GET'])
def get_all (request):
    ticket = Ticket.objects.all()
    serializer = TicketSerializer(ticket, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one (request , pk ):
    try:
        ticket=Ticket.objects.get(user=pk )
        serializer = TicketSerializer(ticket,many = False)
        return Response ({'message':'Ticket request of the user are as follows'},status=status.HTTP_200_OK)
    except:
        return Response({'error': 'No such a User exists'},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def add(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
            
        email = data.get('email')
        user = User.objects.filter(email = email).first()

        if not user:
            return Response({'error':'User with this email Doesnot exists'},status=status.HTTP_204_NO_CONTENT)
        
        ticket = Ticket.objects.create(
            person_name = data.get('name'),
            person_email = email,
            contact_no = data.get('phone'),
            message = data.get('message'),
        )

        ticket.save()

        return Response({'message':'Ticket Raised Successfully'},status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"Error":str(e)},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        # return Response({'error':'Ticket request cannot be generated'},status=status.HTTP_400_BAD_REQUEST)
