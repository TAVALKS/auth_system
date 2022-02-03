from django.urls import path
from .views import (
    ListUsers,
    CustomAuthToken,
    GetInfo,
    RegisterView,
    GetTokenCall)

urlpatterns = [
    path('users', ListUsers.as_view()),
    path('token/auth', CustomAuthToken.as_view()),
    path('get/info', GetInfo.as_view()),
    path('register', RegisterView.as_view()),
    path('token/makecall', GetTokenCall.as_view()),
]
