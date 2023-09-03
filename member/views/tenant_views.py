from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.serializers import TenantSerializer, UserSerializerWithToken
from member.models import Tenant, City, Country, State, Society
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
import json
import random
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from datetime import datetime, timedelta
import os

@api_view(['GET'])
def get_all_tenant(request):
    tenant = Tenant.objects.all()
    serializer = TenantSerializer(tenant, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_tenant(request):
    
    data = request.body

    # Decode the bytes into a string
    data_str = data.decode('utf-8')

    data_dict = json.loads(data_str)

    if not 'dob' in data_dict:
        data_dict['dob'] = date.today()
    
    if not 'hno' in data_dict:
        data_dict['hno']=random.randint(1,1000)
    
    data_dict['area']=Society.objects.filter(area='Ardee City Sector 52').first()
    data_dict['city']=City.objects.filter(city='Gurgaon').first()
    data_dict['state']=State.objects.filter(state='Haryana').first()
    data_dict['country']=Country.objects.filter(country='India').first()
    
    try:
        user = User.objects.create(
            first_name=data_dict['first_name'],
            last_name=data_dict['last_name'],
            username=data_dict['email'],
            email=data_dict['email'],
            password=make_password(data_dict['password'])
        )
        tenant = Tenant.objects.create(
            user = user,
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

    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def generate_otp(request):
    data = request.body

    # Decode the bytes into a string
    data_str = data.decode('utf-8')

    data_dict = json.loads(data_str)

    email = data_dict['email']

    try:
        tenant = Tenant.objects.get(email=email)
    except Tenant.DoesNotExist:
        return Response({"error": "Tenant not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": f"An error occured: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    otp = str(random.randint(1000, 9999))

    tenant.otp = otp
    tenant.save()

    subject = "OTP Verification"
    message = render_to_string('acc_active_email.html', {'nme': data_dict['first_name'], 'otp': otp})
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

    return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def verify_otp(request):
    data = request.body

    data_str = data.decode('utf-8')

    payload = json.loads(data_str)

    user_otp = payload.get('otp')

    try:
        refresh = RefreshToken()
        access_token = refresh.access_token

        expiry_timestamp = access_token.payload['exp']
        current_timestamp = datetime.utcnow().timestamp()
    
        if expiry_timestamp < current_timestamp:
            return Response({"message": "Refresh token has expired"}, status=status.HTTP_401_UNAUTHORIZED)


    except (TokenError, ValueError):
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Tenant.objects.get(otp=user_otp)

        if user.otp == user_otp:
            user.is_verified = True
            user.save()
            return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"error":"OTP formatting"}, status=status.HTTP_400_BAD_REQUEST)

    except Tenant.DoesNotExist:
        return Response({"error": "Tenant not found or Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)