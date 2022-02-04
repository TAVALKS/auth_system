from django.urls import path
from .views import (
    ListUsers,
    CustomAuthToken,
    RegisterView)

urlpatterns = [
    path('users', ListUsers.as_view()),
    path('token/auth', CustomAuthToken.as_view()),
    path('register', RegisterView.as_view()),
]
