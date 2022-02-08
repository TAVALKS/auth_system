from re import A
from rest_framework.response import Response
from django.http import HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import authentication, permissions
from .serializers import UserInfoSerializer, UserCallsSerializer
from .models import UserInfo, MakeCall, UserCalls
from secrets import token_hex
import requests
from datetime import datetime


class GetInfo(APIView):
    """View for get info about a user information:
       calls_remaining, exp, url"""
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        info = UserInfoSerializer(UserInfo.objects.filter(user=user), many = True).data
        mc = MakeCall.objects.get(user=user)
        call_token = mc.call_token
        if len(info) > 0:
            info = info[0]
            info['call_token'] = call_token
        response = Response(
            {'user': info}
        )
        return response


class GetCallsList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        uc = UserCallsSerializer(UserCalls.objects.filter(user=user), many= True).data
        response = Response(
            {'calls': uc}
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
            ui = UserInfo.objects.get(user=user)
            ui.calls_remaining -= 1
            ui.save()
            uc = UserCalls(user=user, out_number=tel, verify_number='+7232',
                      call_date=datetime.now())
            uc.save()
        except MakeCall.DoesNotExist:
            return HttpResponseNotFound()
        requests.post(url='http://127.0.0.1:5000/verify',
                      json={'phone_number': tel})
        response = Response({
            'verify_code': '5521'
        })
        return response
