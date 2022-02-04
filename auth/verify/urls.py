from django.urls import path
from .views import VerifyNumber

urlpatterns = [
    path('makecall', VerifyNumber.as_view()),
]
