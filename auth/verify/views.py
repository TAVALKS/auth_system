from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import authentication, permissions
from .serializers import verify_numberSerializer
from .models import verify_number
from secrets import token_hex
import requests


class GetInfo(APIView):
    """View for get info about a user information:
       calls_remaining, exp, url"""
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        info = verify_numberSerializer(verify_number.objects.filter(user=user), many = True).data
        if len(info) > 0:
            info = info[0]
        response = Response(
            {'user': info}
        )
        return response


class GetTokenCall(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        token = token_hex()
        response = Response(
            {'call_token':token}
        )
        return response


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
        info = verify_numberSerializer(verify_number.objects.filter(user=2), many=True).data
        requests.post(url='http://127.0.0.1:5000/verify', 
                      json={'phone_number': tel})
        if len(info) > 0:
            info = info[0]
        response = Response(
            {'user': info}
        )
        return response
