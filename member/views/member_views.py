from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Member
from django.contrib.auth.models import User
from member.serializers import MemberSerializer, UserSerializerWithToken
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.http import HttpResponse
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

    splitlist = str(data).split('&')

    username_raw = splitlist[0].split('=')[1]
    password_raw = splitlist[1].split('=')[1]

    username = username_raw.replace('%40', '@')
    password = password_raw[0:len(password_raw)-1]

    if username == '' or password == '' or (username == '' and password == ''):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    res = requests.post("http://localhost:8000/token/", data=
                            {
                                'username': username,
                                'password': password
                            })
    
    return Response(data=res.json())