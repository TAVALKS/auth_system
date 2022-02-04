from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth.models import User
from secrets import token_hex
from rest_framework.decorators import authentication_classes, permission_classes
import requests


class RegisterView(ObtainAuthToken):
    """View for registering"""
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'email': user.email
        })


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'email': user.email
        })


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