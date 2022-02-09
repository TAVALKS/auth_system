from django.urls import path
from .views import (
    ListUsers,
    CustomAuthToken,
    RegisterView,
    )
from .PasswordResetView import CustomPasswordResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users', ListUsers.as_view()),
    path('token/auth', CustomAuthToken.as_view()),
    path('register', RegisterView.as_view()),
    path('password_reset', CustomPasswordResetView.as_view()),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
]
