from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.serializers import TenantSerializer, UserSerializerWithToken
from member.models import Tenant
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
import json
import random
from datetime import date

@api_view(['GET'])
def get_all_tenant(request):
    tenant = Tenant.objects.all()
    serializer = TenantSerializer(tenant, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registration_tenant(request):
    
    data = request.body

    # Decode the bytes into a string
    data_str = data.decode('utf-8')

    data_dict = json.loads(data_str)

    data_dict['dob']=date.today()
    data_dict['hno']=random.randint(1,1000)
    data_dict['area']=1
    data_dict['city']=1
    data_dict['state']=1
    data_dict['country']=1
    
    try:
        user = User.objects.create(
            first_name=data_dict['first_name'],
            last_name=data_dict['last_name'],
            username=data_dict['email'],
            email=data_dict['email'],
            password=make_password(data_dict['password'])
        )
        tenant = Tenant.objects.create(
            fname = data_dict['first_name'],
            lname = data_dict['last_name'],
            gender = data_dict['gender'],
            email = data_dict['email'],
            phone_no = data_dict['phone'],
            date_of_birth = data_dict['dob'],
            res_hno = data_dict['hno'],
            res_area = data_dict['area'],
            res_city = data_dict['city'],
            res_state = data_dict['state'],
            res_country = data_dict['country'],
        )
        # when we register a user, we need to return the token
        serializer = UserSerializerWithToken(user, many=False)
        slz = TenantSerializer(tenant, many=False)

        message = {'User': serializer.data, 'Tenant': slz.data}
        return Response(message, status=status.HTTP_200_OK)

    except:
        message = {'error': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)




