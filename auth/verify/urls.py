from django.urls import path
from .views import (
    VerifyNumber,
    GetCallToken,
    GetInfo,
    GetCallsList,
    SetUserInfo)

urlpatterns = [
    path('info', GetInfo.as_view()),
    path('get/calltoken', GetCallToken.as_view()),
    path('makecall/<token>', VerifyNumber.as_view()),
    path('calls', GetCallsList.as_view()),
    path('set/user/info', SetUserInfo.as_view()),
]