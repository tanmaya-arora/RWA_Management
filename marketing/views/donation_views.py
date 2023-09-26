import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from marketing.models import Campaign, Event
from internal.serializers import CampaignSerializer
from user_management.models import Owner


# @api_view(['GET'])
# def get_all_donations(request):
#     donations = Campaign.objects.all()
#     serializer = CampaignSerializer(donations, many=True)
#     message = {'Info': 'All donation details fetched successfully', 'data': serializer.data}
#     return Response(message, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def add_donation(request):
#     body = request.body
#     data_str = body.decode('utf-8')
#     data = json.loads(data_str)

#     try:
#         member_obj = Owner.objects.filter(email=data['user_email']).first()
#         # slz = MemberSerializer(member_obj, many=False)
#         # member = slz.data

#         if not 'note' in data:
#             data['note'] = f"Member donated Rs. {data['donation_amount']} to the RWA"
        
#         campaign = Campaign.objects.create(
#             member = member_obj,
#             donation_amount = data['donation_amount'],
#             event = Event.objects.filter(event_name=data['event_name']).first(),
#             notes = data['note']
#         )

#         serializer = CampaignSerializer(campaign, many=False)
#         message = {'Info': 'Donation done successfully', 'donation': serializer.data}

#         return Response(message, status=status.HTTP_200_OK)
#     except Exception as e:
#         message = {'error': str(e)}
#         return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_all_donations(request):
    donations = Campaign.objects.all()
    serializer = CampaignSerializer(donations, many=True)
    
    total_donation_till_now = sum([donation.donation_amount for donation in donations])
    
    message = {
        'Info': 'All donation details fetched successfully',
        'data': serializer.data,
        'total_donation_till_now': total_donation_till_now
    }
    
    return Response(message, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_donation(request):
    body = request.body
    data_str = body.decode('utf-8')
    data = json.loads(data_str)

    try:
        member_obj = Owner.objects.filter(email=data['user_email']).first()

        if not 'note' in data:
            data['note'] = f"Member donated Rs. {data['donation_amount']} to the RWA"
        
        event = Event.objects.filter(event_name=data['event_name']).first()
        
        # Calculate donations for a single event
        event_donations = Campaign.objects.filter(event=event)
        total_event_donation = sum([donation.donation_amount for donation in event_donations])
        
        campaign = Campaign.objects.create(
            member=member_obj,
            donation_amount=data['donation_amount'],
            event=event,
            notes=data['note']
        )

        serializer = CampaignSerializer(campaign, many=False)
        message = {
            'Info': 'Donation done successfully',
            'donation': serializer.data,
            'total_event_donation': total_event_donation
        }

        return Response(message, status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
