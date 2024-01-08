from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_management.models import Family
from internal.serializers import FamilyMemberSerializer
import json
from datetime import date
from django.contrib.auth.models import User;


@api_view(['GET'])
def get_family_members(request):
    member = Family.objects.all()
    serializer = FamilyMemberSerializer(member, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_sepecific_family(request,pk):
    try:
        family_members = Family.objects.filter(family_head__email=pk)

        if family_members.exists():
            serializer = FamilyMemberSerializer(family_members, many=True)
            message = {'info': 'Family details fetched successfully', 'data': serializer.data}
            return Response(message, status=status.HTTP_200_OK)
        else:
            message = {'error': 'Member not found'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)

    except Family.DoesNotExist:
        message = {'error': 'No Family Member registered for this user'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def register_family_member(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    if data_dict['family_head'] != '':
        user = User.objects.filter(email=data_dict['family_head']).first()
    else:
        user = None


    if 'dob' not in data_dict:
        data_dict['dob'] = date.today()

    if ' ' in data_dict['first_name']:
        splitname = data_dict['first_name'].split(' ')
        data_dict['first_name'] = splitname[0]
        data_dict['last_name'] = splitname[-1]
    
    if not 'last_name' in data_dict:
        data_dict['last_name'] = ''
    
    if 'aniversary_date' in data_dict:    
        familymember = Family.objects.create(
            gender=data_dict['gender'],
            date_of_birth=data_dict['dob'],
            relation=data_dict['relation'],
            fname=data_dict['first_name'],
            lname=data_dict['last_name'],
            aniversary_date=data_dict['aniversary_date'],
            marital_status=data_dict['marriedCheck'],
            family_head=user
        )
    else:
        familymember = Family.objects.create(
            gender=data_dict['gender'],
            date_of_birth=data_dict['dob'],
            relation=data_dict['relation'],
            fname=data_dict['first_name'],
            lname=data_dict['last_name'],
            marital_status=data_dict['marriedCheck'],
            family_head=user
        )
        

    serializer = FamilyMemberSerializer(familymember)
    message = {
        'Info': 'Family Member added successfully.',
        'FamilyMember': serializer.data
    }
    return Response(message, status=status.HTTP_200_OK)
