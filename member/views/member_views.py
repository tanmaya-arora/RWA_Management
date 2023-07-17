from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Member
from django.contrib.auth.models import User
from member.serializers import MemberSerializer, UserSerializerWithToken
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.http import HttpResponse, QueryDict
import requests


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
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_member(request):
    data = request.body

    #splitlist = str(data).split('&')

    #username_raw = splitlist[0].split('=')[1]
    #password_raw = splitlist[1].split('=')[1]

    parsed_body = QueryDict(data.decode())
    
    print("Parsed body in login_members is ",parsed_body)
    
    username = parsed_body.get('username')
    password = parsed_body.get('password')

    print("Username final is ",username)
    print("Password final is ",password)
    
    if username == '' or username != None or password == '' or \
        password != None or ((username == '' or username != None) and \
                             (password == '' or password != None)):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    res = requests.post("http://localhost:8000/token/", data=
                            {
                                'username': username,
                                'password': password
                            })
    
    return Response(data=res.json())