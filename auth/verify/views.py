from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
import requests


@authentication_classes([])
@permission_classes([])
class VerifyNumber(APIView):

    def post(self, request):
        tel = request.data['tel']
        token = request.data['token']
        response = Response({
            'token': token,
            'tel': tel,
        })
        requests.post(url='http://127.0.0.1:5000/verify', 
                      json={'phone_number': tel})
        return response