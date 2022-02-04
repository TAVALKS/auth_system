from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes

# Create your views here.
@authentication_classes([])
@permission_classes([])
class VerifyNumber(APIView):

    def post(self, request):
        tel = request.data['tel']
        token= request.data['token']
        return Response({
            'token': token,
            'tel': tel
        })