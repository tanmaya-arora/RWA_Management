from rest_framework.decorators import api_view
from rest_framework.response import Response
from internal.serializers import TenantSerializer, UserSerializerWithToken
from internal.models import City, Country, State, Society
from user_management.models import Tenant
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

@api_view(['GET'])
def get_tenant(request, pk):
    try:    
        tenant = Tenant.objects.get(tenant_id = pk)
        serializer = TenantSerializer(tenant, many = False)
        message = {'Info':'Member details fetched successfully', 'data':serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except:
        message = {'error':'Member does not exists'}
        return Response(message, status=status.HTTP_303_SEE_OTHER)
    
@api_view(['POST'])
def generate_otp(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    email = data_dict.get('email')
    
    try:
        tenant = Tenant.objects.get(email=email)
    except Tenant.DoesNotExist:
        return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    otp = str(random.randint(1000, 9999))

    tenant.otp = otp
    tenant.save()

    subject = "Your OTP Code"
    message = f"Your OTP code is: {otp}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

    return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)

            
@api_view(['POST'])
def verify_jwt(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    otp = data_dict.get('otp')

    try:
        refresh = RefreshToken()
        access_token = refresh.access_token
        user_id = access_token.payload.get('email')

        refresh_token_validity = int(os.getenv("REFRESH_TOKEN_VALIDITY", 30)) 

        expiry_timestamp = access_token.payload['exp']
        current_timestamp = datetime.utcnow()
        refresh_token_expiry_time = current_timestamp + timedelta(seconds=refresh_token_validity)
        
        if expiry_timestamp < refresh_token_expiry_time.timestamp():
            return Response({"message": "Refresh token has expired"}, status=status.HTTP_401_UNAUTHORIZED)
        

    except (TokenError, ValueError):
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = Tenant.objects.get(otp=otp)

        if user.otp == otp:
            user.isVerified = True
            user.save()
            return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"error":"OTP formatting"})
        
    except Tenant.DoesNotExist:
        return Response({"error": "Member not found or Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_tenant(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str )
  
    if not 'dob' in data_dict:
        data_dict['dob'] = date.today()

    data_dict['area'] = Society.objects.filter(area='Ardee City Sector 52').first()
    data_dict['city'] = City.objects.filter(city='Gurgaon').first()
    data_dict['state'] = State.objects.filter(state='Haryana').first()
    data_dict['country'] = Country.objects.filter(country='India').first()

    try:
        email = data_dict.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            return Response({"error": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            first_name=data_dict['first_name'],
            last_name=data_dict['last_name'],
            username=email,
            email=email,
            password=make_password(data_dict['password'])
        )    

        tenant = Tenant.objects.create(
            user=user, 
            fname=data_dict['first_name'],
            lname=data_dict['last_name'],
            gender=data_dict['gender'],
            email=email,
            phone_no=data_dict['phone'],
            date_of_birth=data_dict['dob'],
            res_hno=data_dict['hno'],
            res_area=data_dict['area'],
            res_city=data_dict['city'],
            res_state=data_dict['state'],
            res_country=data_dict['country'],
        )

        response_data = {
            "message": "User registered successfully. Please check your email for verification."
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
            

    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_tenant(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    email = data_dict.get('email')
    password = data_dict.get('password')

    tenant = Tenant.objects.get(email=email)
    
    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return Response({"error": "Invalid credentials : user id or password may be incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not tenant.isVerified:
            return Response({"error": "User is not verified", 'isVerified':False}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({"access_token": access_token, "user_type":"Tenant"}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def reset_password(request):
    try:
        data = request.body
        data_str = data.decode('utf-8')
        data_dict = json.loads(data_str)

        email = data_dict.get('email')
        password = data_dict.get('password')
        cnfpassword = data_dict.get('cnfpassword')

        if password != cnfpassword:
            return Response({"error": "New password and confirmation password do not match"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()

        return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({"error": "User with provided email not found"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)