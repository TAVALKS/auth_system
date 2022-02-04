from django.urls import path
from .views import VerifyNumber, GetCallToken, GetInfo

urlpatterns = [
    path('info', GetInfo.as_view()),
    path('get/calltoken', GetCallToken.as_view()),
    path('makecall', VerifyNumber.as_view()),
]
