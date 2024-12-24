from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import DataSerializer
from data.models import CustomUser

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def data_api(request):
    data_var = CustomUser.objects.all()
    serializer = DataSerializer(data_var, many=True)
    return Response(serializer.data)
