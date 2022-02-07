from rest_framework.response import Response
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import authentication, permissions
from .serializers import verify_numberSerializer
from .models import verify_number, MakeCall
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


class GetCallToken(APIView):
    '''View for get call token or generate'''
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        try:
            mc = MakeCall.objects.get(user=user)
            token = mc.call_token
        except MakeCall.DoesNotExist:
            token = token_hex()
            mc = MakeCall(user=user, call_token=token)
            mc.save()
        response = Response(
            {'call_token':token,
             'user': user.username}
        )
        return response


@authentication_classes([])
@permission_classes([])
class VerifyNumber(APIView):

    def post(self, request):
        tel = request.data['tel']
        token = request.data['token']
        try:
            mc = MakeCall.objects.get(call_token=token)
            user = mc.user
        except MakeCall.DoesNotExist:
            return HttpResponseNotFound()
        requests.post(url='http://127.0.0.1:5000/verify',
                      json={'phone_number': tel})
        response = Response({
            'token': token,
            'tel': tel
        })
        return response
