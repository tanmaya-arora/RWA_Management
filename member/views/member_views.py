from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Member
from django.contrib.auth.models import User
from member.serializers import MemberSerializer, UserSerializerWithToken
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.http import HttpResponse, QueryDict
import requests
import json


@api_view(['GET'])
def get_all_members(request):
    member = Member.objects.all()
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_member(request):
    data = request.body

    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        # when we register a user, we need to return the token
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists', 'data': data}
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

    print("Username final is ",username)
    print("Password final is ",password)
    
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