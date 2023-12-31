from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_management.models import Owner
from internal.models import City, Country, Society, State
from user_management.models import Owner
from django.contrib.auth.models import User
from internal.serializers import MemberSerializer
from django.contrib.auth.hashers import make_password
from datetime import date, datetime, timedelta
import random
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import status
import json
import os

@api_view(['GET'])
def get_all_members(request):
    member = Owner.objects.all()
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_member(request, pk):
    try:    
        member = Owner.objects.get(member_id = pk)
        serializer = MemberSerializer(member, many = False)
        message = {'Info':'Member details fetched successfully', 'data':serializer.data}
        return Response(message, status=status.HTTP_200_OK)
    except:

        try:
            member = Owner.objects.get(user_id = pk)
            serializer = MemberSerializer(member, many = False)
            message = {'Info':'Member details fetched successfully', 'data':serializer.data}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:

            message = {'error':str(e)}
            return Response(message, status=status.HTTP_303_SEE_OTHER)

@api_view(['POST'])
def generate_otp(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    email = data_dict.get('email')
    
    try:
        member = Owner.objects.get(email=email)
    except Owner.DoesNotExist:
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
        user = Owner.objects.get(otp=otp)

        if user.otp == otp:
            user.isVerified = True
            user.save()
            return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"error":"OTP formatting"})
        
    except Owner.DoesNotExist:
        return Response({"error": "Member not found or Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_member(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
      
    if not 'dob' in data_dict:
        data_dict['dob'] = date.today()
        
    if not 'hno' in data_dict:
        data_dict['hno'] = random.randint(1, 1000)

    data_dict['area'] = Society.objects.filter(area='Ardee City Sector 52').first()
    data_dict['city'] = City.objects.filter(city='Gurgaon').first()
    data_dict['state'] = State.objects.filter(state='Haryana').first()
    data_dict['country'] = Country.objects.filter(country='India').first()

    try:
        email = data_dict.get('email')
        hno = data_dict.get('hno')
        user = User.objects.filter(email=email).first()
        hno_owner = Owner.objects.filter(res_hno = hno).first()
        
        if user:
            return Response({"error": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if hno_owner:
            return Response({"error": "House No Already registed with the other owner"}, status= status.HTTP_303_SEE_OTHER)
        
        user = User.objects.create(
            first_name=data_dict['first_name'],
            last_name=data_dict['last_name'],
            username=email,
            email=email,
            password=make_password(data_dict['password'])
        )

        if 'anniversary_date' in data_dict:
            member = Owner.objects.create(
                user=user,
                fname=data_dict['first_name'],
                lname=data_dict['last_name'],
                gender=data_dict['gender'],
                email=email,
                phone_no=data_dict['phone'],
                date_of_birth=data_dict['dob'],
                aniversary_date=data_dict['anniversary_date'],
                marital_status=data_dict['marriedCheck'],
                res_hno=hno,
                res_area=data_dict['area'],
                res_city=data_dict['city'],
                res_state=data_dict['state'],
                res_country=data_dict['country'],
            )    

        else:
            member = Owner.objects.create(
                user=user, 
                fname=data_dict['first_name'],
                lname=data_dict['last_name'],
                gender=data_dict['gender'],
                email=email,
                phone_no=data_dict['phone'],
                date_of_birth=data_dict['dob'],
                marital_status=data_dict['marriedCheck'],
                res_hno=hno,
                res_area=data_dict['area'],
                res_city=data_dict['city'],
                res_state=data_dict['state'],
                res_country=data_dict['country'],
            )

        response_data = {
            "message": "User registered successfully."
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
            

    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_member(request):
    data = request.body
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)

    email = data_dict.get('email')
    password = data_dict.get('password')

    try:
        member = Owner.objects.get(email=email)
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return Response({"error": "Invalid credentials : user id or password may be incorrect"}, status=status.HTTP_400_BAD_REQUEST )
        
        if not member.isVerified:
            return Response({"error": "User is not verified", 'isVerified':False}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({"access_token": access_token,"user_type": "Owner"}, status=status.HTTP_200_OK)
    except Owner.DoesNotExist:
        return Response({"error": "Owner is not registered with the RWA"}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
    return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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


