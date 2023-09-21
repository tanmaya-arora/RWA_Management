from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from support.models import Ticket, TicketReply
from internal.serializers import TicketSerializer
import json
from django.contrib.auth.models import User, Group

@api_view(['GET'])
def get_all (request):
    ticket = Ticket.objects.all()
    serializer = TicketSerializer(ticket, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one(request, pk):
    try:
        ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(ticket, many=False)
        return Response(serializer.data)
    except Ticket.DoesNotExist:
        return Response({'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)

    
@api_view(['POST'])
def add(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        email = data.get('email')  
        user = User.objects.filter(email=email).first()

        if not user:
            return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)

        existing_ticket = Ticket.objects.filter(person_email=email, resolved=False).first()
        if existing_ticket:
            return Response({'error': 'A ticket has already been raised for this user'}, status=status.HTTP_400_BAD_REQUEST)

        ticket = Ticket.objects.create(
            person_name=data.get('name'),
            person_email=email,
            contact_no=data.get('phone'),
            message=data.get('message'),
            priority=data.get('priority')
        )

        return Response({'message': 'Ticket Raised Successfully'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
@api_view(['POST'])
def reply(request):
    data = json.loads(request.body.decode('utf-8'))

    name  = data.get('name')
    try:
        ticket_id = data.get('ticket_id')
        ticket = Ticket.objects.filter(pk=ticket_id).first()

        if not ticket:
            return Response({'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)

        ticket_reply = TicketReply.objects.create(
            ticket=ticket,
            reply_message=data.get('message'),
            replied_by = Group.objects.get(name = name ),
        )

        return Response({'message': 'Reply to this ticket successful'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"Error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)