from rest_framework import serializers
from .models import UserInfo, UserCalls

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['url', 'calls_remaining', 'exp', 'balance', 'coast_call']


class UserCallsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCalls
        fields = ['user', 'out_number', 'verify_number', 'call_date', 'coast']