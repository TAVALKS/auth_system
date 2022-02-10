from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from rest_framework.views import APIView


@authentication_classes([])
@permission_classes([])
class CustomPasswordResetView(APIView):
    # Реализуйте запрос "почтовый ящик не зарегистрирован"
    def post(self, request, format=None):
        data = request.data['email']
        associated_users = User.objects.filter(Q(email=data))
        if associated_users.exists():
            for user in associated_users:
                subject = "Password Reset Requested"
                email_template_name = "password_reset_email.txt"
                c = {
                "email":user.email,
                'domain':'127.0.0.1:8000',
                'site_name': 'Website',
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                'token': default_token_generator.make_token(user),
                'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, 'bot@chzmk.com' , [user.email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponse(f'Письмо со ссылкой сброса пароля выслано на эл.почту: {user.email}')
        else:
            return Response(f'Адрес электронной почты: {data} не зарегистрирован')
