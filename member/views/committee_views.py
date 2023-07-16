from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Committee
from member.serializers import CommitteeSerializer


@api_view(['GET'])
def get_all_committees(request):
    committee = Committee.objects.all()
    serializer = CommitteeSerializer(committee, many=True)
    return Response(serializer.data)