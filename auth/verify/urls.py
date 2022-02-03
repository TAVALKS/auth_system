from django.urls import path
from .views import VerifyNumber

urlpatterns = [
    path('makecall/<token>/<tel>', VerifyNumber.as_view()),
]
