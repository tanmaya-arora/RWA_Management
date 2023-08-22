from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Member
from django.contrib.auth.models import User
from member.serializers import MemberSerializer, UserSerializer, UserSerializerWithToken
from django.contrib.auth.hashers import make_password
from rest_framework import status
import requests
import json
from datetime import date
import random

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
        )
        # when we register a user, we need to return the token
        slz = MemberSerializer(member, many=False)
        serializer = UserSerializerWithToken(user, many=False)
        message = {'User': serializer.data, 'Member': slz.data}
        return Response(message, status=status.HTTP_200_OK)

    except Exception as e:
        message = {'error': e}
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
    
    username = data_dict['username']
    password = data_dict['password']

    # print("Username final is ",username)
    # print("Password final is ",password)
    
    if username == '' or username == None or password == '' or \
        password == None or ((username == '' or username == None) and \
                             (password == '' or password == None)):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    res = requests.post("https://lobster-app-et3xm.ondigitalocean.app/token/", data=
                            {
                                'username': username,
                                'password': password
                            })
    
    return Response(data=res.json())

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