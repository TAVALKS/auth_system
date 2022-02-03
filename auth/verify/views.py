from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
# Create your views here.


@authentication_classes([])
@permission_classes([])
class VerifyNumber(APIView):

    def post(self, request, token, tel):
        return Response({
            'token': token,
            'tel': tel
        })