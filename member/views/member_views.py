from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Member, City, Country, Society, State
from django.contrib.auth.models import User
from member.serializers import MemberSerializer
from django.contrib.auth.hashers import make_password
from datetime import date, datetime, timedelta
import random
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import status
import json
from rest_framework import status
import os

@api_view(['GET'])
def get_all_members(request):
    member = Member.objects.all()
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_member(request, pk):
    try:    
        member = Member.objects.get(member_id = pk)
        serializer = MemberSerializer(member, many = False)
        message = {'Info':'Member details fetched successfully', 'data':serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except:
        message = {'error':'Member does not exists'}
        return Response(message, status=status.HTTP_303_SEE_OTHER)

@api_view(['POST'])
def generate_otp(request):
    email = request.data.get('email')
    
    try:
        member = Member.objects.get(email=email)
    except Member.DoesNotExist:
        return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    otp = str(random.randint(1000, 9999))

    member.otp = otp
    member.save()

    subject = "Your OTP Code"
    message = f"Your OTP code is: {otp}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

    return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)

            
@api_view(['POST'])
def verify_jwt(request):
    otp = request.data.get('otp')
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
        user = Member.objects.get(otp=otp)

        if user.otp == otp:
            user.is_verified = True
            user.save()
            return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"error":"OTP formatting"})
        
    except Member.DoesNotExist:
        return Response({"error": "Member not found or Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_member(request):
    data = request.data
  
    if not 'dob' in data:
        data['dob'] = date.today()

    data['hno'] = random.randint(1, 1000)
    data['area'] = Society.objects.filter(area='Ardee City Sector 52').first()
    data['city'] = City.objects.filter(city='Gurgaon').first()
    data['state'] = State.objects.filter(state='Haryana').first()
    data['country'] = Country.objects.filter(country='India').first()

    try:
        email = data.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            return Response({"error": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=email,
            email=email,
            password=make_password(data['password'])
        )    

        member = Member.objects.create(
            user=user, 
            fname=data['first_name'],
            lname=data['last_name'],
            gender=data['gender'],
            email=email,
            phone_no=data['phone'],
            date_of_birth=data['dob'],
            res_hno=data['hno'],
            res_area=data['area'],
            res_city=data['city'],
            res_state=data['state'],
            res_country=data['country'],
        )

        response_data = {
            "message": "User registered successfully. Please check your email for verification."
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)
            

    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_member(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return Response({"error": "Invalid credentials : user id or password may be incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.member.is_verified:
            return Response({"error": "User is not verified"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({"access_token": access_token}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def reset_password(request):
    try:
        data = request.data
        email = data.get('email')
        password = data.get('password')
        cnfpassword = data.get('cnfpassword')

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

# @api_view(['POST'])
# def send_email_to_client(request):
#     try:
#         data = request.data
#         data_str = data.decode('utf-8')
#         data_dict = json.loads(data_str)

#         print("Data dict ",data_dict)
        
#         subject = "Confirm Email"
#         message = render_to_string('acc_active_email.html', {'nme': data_dict['username']})
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [data_dict['recipient']]
#         send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

#         return Response(status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
