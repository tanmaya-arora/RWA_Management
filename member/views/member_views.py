from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Member, City, Country, Society, State, Tenant
from django.contrib.auth.models import User
from member.serializers import MemberSerializer, UserSerializer, UserSerializerWithToken
from django.contrib.auth.hashers import make_password
from rest_framework import status
import requests
import json
from datetime import date
import random
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import time

@api_view(['GET'])
def get_all_members(request):
    member = Member.objects.all()
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_member(request):
    data = request.body

    # Decode the bytes into a string
    data_str = data.decode('utf-8')

    data_dict = json.loads(data_str)
    
    # splitlist = str(data).split('&')
    
    # name = splitlist[0].split('=')[1]
    # email_raw = splitlist[1].split('=')[1]
    # password_raw = splitlist[2].split('=')[1]
    
    # email = email_raw.replace('%40', '@')
  
    if not 'dob' in data_dict:
        data_dict['dob']=date.today()
    
    data_dict['hno']=random.randint(1,1000)
    data_dict['area']=Society.objects.filter(area='Ardee City Sector 52').first()
    data_dict['city']=City.objects.filter(city='Gurgaon').first()
    data_dict['state']=State.objects.filter(state='Haryana').first()
    data_dict['country']=Country.objects.filter(country='India').first()
    
    try:
        user_obj = User.objects.create(
            first_name=data_dict['first_name'],
            last_name=data_dict['last_name'],
            username=data_dict['email'],
            email=data_dict['email'],
            password=make_password(data_dict['password'])
        )
        
        # when we register a user, we need to return the token
        serializer = UserSerializerWithToken(user_obj, many=False)
        
        member = Member.objects.create(
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
            user = User.objects.filter(email=data_dict['email']).first()
        )

        slz = MemberSerializer(member, many=False)
        message = {'User': serializer.data, 'Member': slz.data}

        return Response(message, status=status.HTTP_200_OK)

    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_member(request):
    data = request.body

    # Decode the bytes into a string
    data_str = data.decode('utf-8')
    
    #splitlist = str(data).split('&')

    #username_raw = splitlist[0].split('=')[1]
    #password_raw = splitlist[1].split('=')[1]

    data_dict = json.loads(data_str)

    #parsed_body = QueryDict(data.decode('utf-8'))
    
    #print("Parsed body in login_members is ",parsed_body)
    
    useremail = data_dict['user_email']
    password = data_dict['password']

    # print("Username final is ",username)
    # print("Password final is ",password)

    member = Member.objects.filter(email=useremail).first()
    tenant = Tenant.objects.filter(email=useremail).first()
    
    
    # if useremail == '' or useremail == None or password == '' or \
    #     password == None or ((useremail == '' or useremail == None) and \
    #                          (password == '' or password == None)):
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    if member == None and tenant == None:
        try:
            user_obj = User.objects.get(email=useremail)
            serializer = UserSerializer(user_obj, many=False)
            user = serializer.data

            if user['is_superuser']:
                res = requests.post("https://lobster-app-et3xm.ondigitalocean.app/token/", data=
                                {
                                    'username': useremail,
                                    'password': password
                                })
                
                return Response(data=res.json())
        except Exception as e:
            message = {'error': str(e)}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    elif member != None:
        member_obj = Member.objects.get(email=useremail)
        token = requests.post("https://lobster-app-et3xm.ondigitalocean.app/token/", data=
                                {
                                    'username': useremail,
                                    'password': password
                                })
        res = token.json()
        res['person_name'] = member_obj.fname
        res['user_type'] = 'Owner'
        
        return Response(data=res)
    else:
        tenant_obj = Tenant.objects.get(email=useremail)
        token = requests.post("https://lobster-app-et3xm.ondigitalocean.app/token/", data=
                                {
                                    'username': useremail,
                                    'password': password
                                })
        res = token.json()
        res['person_name'] = tenant_obj.fname
        res['user_type'] = 'Tenant'
        
        return Response(data=res)

@api_view(['POST'])
def reset_password(request):
    data = request.body

    splitlist = str(data).split('&')
    
    email_raw = splitlist[0].split('=')[1]
    password_raw = splitlist[1].split('=')[1]
    cnfpassword_raw = splitlist[2].split('=')[1]

    email = email_raw.replace('%40', '@')
    password = password_raw.strip()
    cnfpassword = cnfpassword_raw.strip("'")

    userr = User.objects.get(email=email)   
    serializer = UserSerializer(userr, many=False)
    user = serializer.data
    
    if password != cnfpassword:
        message = {'error': 'New password and confirmation password do not match'}

        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    user['password'] = make_password(password)
    
    user.save()

    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def send_email_to_client(request):
    try:
        data = request.body

        # Decode the bytes into a string
        data_str = data.decode('utf-8')

        data_dict = json.loads(data_str)

        print("Data dict ",data_dict)
        
        subject = "Confirm Email"
        message = render_to_string('acc_active_email.html', {'nme': data_dict['username']})
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [data_dict['recipient']]
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        message = {'error': str(e)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def send_otp(request):
    data = request.body

    data_str = data.decode('utf-8')

    payload = json.loads(data_str)

    email = payload.get('email')  

    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    request.session['otp'] = otp
    request.session['otp_timestamp'] = int(time.time()) 

    subject = "OTP Verification"
    message = render_to_string('acc_active_email.html', {'nme': payload['first_name'], 'otp': otp})
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    try:
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
        return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def verify_otp(request):
    data = request.body

    data_str = data.decode('utf-8')

    payload = json.loads(data_str)

    user_otp = payload.get('otp')

    if not user_otp:
        return Response({"error": "OTP is missing"}, status=status.HTTP_400_BAD_REQUEST)

    stored_otp = request.session.get('otp')

    if not stored_otp:
        return Response({"error": "OTP session data expired or missing"}, status=status.HTTP_400_BAD_REQUEST)

    otp_timestamp = request.session.get('otp_timestamp')

    expiration_interval = 60  

    current_timestamp = int(time.time())

    if current_timestamp - otp_timestamp > expiration_interval:
        return Response({"error": "OTP has expired"}, status=status.HTTP_400_BAD_REQUEST)
    
    if user_otp == stored_otp:
        del request.session['otp']        
        return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)