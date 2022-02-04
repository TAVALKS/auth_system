from rest_framework import serializers
from .models import verify_number

class verify_numberSerializer(serializers.ModelSerializer):

    class Meta:
        model = verify_number
        fields = ['url', 'calls_remaining', 'exp']