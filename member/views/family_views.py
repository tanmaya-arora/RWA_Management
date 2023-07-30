from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import FamilyMember
from member.serializers import FamilyMemberSerializer
import json


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

    familymember = FamilyMember.objects.create(
        gender=data_dict['gender'],
        dob=data_dict['dob'],
        relation=data_dict['relation'],
        person_name=data_dict['person_name'],
    )

    serializer = FamilyMemberSerializer(familymember)
    
    return Response(message={
        'message': 'Family Member added successfully.',
        'FamilyMember': serializer.data
        },
        status=status.HTTP_200_OK
    )