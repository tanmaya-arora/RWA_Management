from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_management.models import FamilyMember
from internal.serializers import FamilyMemberSerializer
import json
from datetime import date
from django.contrib.auth.models import User;


@api_view(['GET'])
def get_family_members(request):
    member = FamilyMember.objects.all()
    serializer = FamilyMemberSerializer(member, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_family_member(request):
    data = request.body

    # Decode the bytes into a string
    data_str = data.decode('utf-8')

    data_dict = json.loads(data_str)

    if data_dict['family_head'] != '':
        user = User.objects.filter(email=data_dict['family_head']).first()
    else:
        user = None


    if 'dob' not in data_dict:
        data_dict['dob'] = date.today()

    if 'anniversary_date' not in data_dict:
        data_dict['anniversary_date'] = date.today()

    if ' ' in data_dict['first_name']:
        splitname = data_dict['first_name'].split(' ')
        data_dict['first_name'] = splitname[0]
        data_dict['last_name'] = splitname[-1]
    
    familymember = FamilyMember.objects.create(
        gender=data_dict['gender'],
        date_of_birth=data_dict['dob'],
        relation=data_dict['relation'],
        fname=data_dict['first_name'],
        lname=data_dict['last_name'],
        aniversary_date=data_dict['anniversary_date'],
        marital_status=data_dict['marriedCheck'],
        family_head=user
    )

    serializer = FamilyMemberSerializer(familymember)
    message = {
        'Info': 'Family Member added successfully.',
        'FamilyMember': serializer.data
    }
    return Response(message, status=status.HTTP_200_OK)
