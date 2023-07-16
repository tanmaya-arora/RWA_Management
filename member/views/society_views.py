from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Society
from member.serializers import SocietySerializer


@api_view(['GET'])
def get_all_societies(request):
    society = Society.objects.all()
    serializer = SocietySerializer(society, many=True)
    return Response(serializer.data)