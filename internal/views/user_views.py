from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from internal.serializers import UserSerializer


@api_view(['GET'])
def get_portal_users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    message = {'Info': 'All users fetched successfully', 'data': serializer.data}
    return Response(message, status=status.HTTP_200_OK)