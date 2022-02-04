from django.urls import path
from .views import VerifyNumber, GetTokenCall, GetInfo

urlpatterns = [
    path('info', GetInfo.as_view()),
    path('makecall', VerifyNumber.as_view()),
    path('get/calltoken', GetTokenCall.as_view()),
]
