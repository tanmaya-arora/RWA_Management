from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.serializers import tenantSerializer
from member.models import Tenant

@api_view(['GET'])
def get_all_tenant (request):
    tenant = Tenant.objects.all()
    Serializer = tenantSerializer (tenant)
    return Response(Serializer.data)



