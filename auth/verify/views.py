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
        uif = UserInfo.objects.filter(user=user)
        if uif.exists():
            info = UserInfoSerializer(uif, many = True).data
            info = info[0]
        else:
            info = {}
        if MakeCall.objects.filter(user=user).exists():
            mc = MakeCall.objects.get(user=user)
            call_token = mc.call_token
        else:
            call_token = token_hex()
            mc = MakeCall(user=user, call_token=call_token)
            mc.save()
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

    def post(self, request, token):
        tel = '+7'+ request.data['tel']
        host = '127.0.0.1'
        r = requests.post(url=f'http://{host}:5000/verify',
                          json={'tel': tel})
        sip = str(r.json()['sip'])
        code = sip[-4:]
        try:
            mc = MakeCall.objects.get(call_token=token)
            user = mc.user
            ui = UserInfo.objects.get(user=user)
            ui.calls_remaining -= 1
            ui.balance = round(ui.balance - ui.coast_call, 2)
            ui.save()
            uc = UserCalls(user=user, out_number=tel, verify_number=sip,
                           call_date=datetime.now(), coast=ui.coast_call)
            uc.save()
        except MakeCall.DoesNotExist:
            return HttpResponseNotFound()
        response = Response({'code': code})
        return response


class SetUserInfo(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        url = request.data['url']
        balance = request.data['balance']
        uif = UserInfo.objects.filter(user=user)
        if uif.exists():
            uif.update(url=url, balance=balance)
            response = 'Изменения сохранены'
            return Response(response)
        else:
            ui = UserInfo(user=user, url=url, balance=balance)
            ui.save()
            response = 'Данные внесены'
        return Response(response)
