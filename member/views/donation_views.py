import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from member.models import Donation, Member
from member.serializers import DonationSerializer


@api_view(['GET'])
def get_all_donations(request):
    donations = Donation.objects.all()
    serializer = DonationSerializer(donations, many=True)
    message = {'Info': 'All donation details fetched successfully', 'data': serializer.data}
    return Response(message, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_donation(request):
    body = request.body
    data_str = body.decode('utf-8')
    data = json.loads(data_str)

    try:
        member_obj = Member.objects.filter(email=data['user_email']).first()
        # slz = MemberSerializer(member_obj, many=False)
        # member = slz.data

        if not 'note' in data:
            data['note'] = f"Member donated Rs. {data['donation_amount']} to the RWA"
        
        donation = Donation.objects.create(
            member = member_obj,
            donation_amount = data['donation_amount'],
            notes = data['note']
        )

        serializer = DonationSerializer(donation, many=False)
        message = {'Info': 'Donation done successfully', 'donation': serializer.data}

        return Response(message, status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

