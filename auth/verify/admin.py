from django.contrib import admin
from .models import verify_number, MakeCall

# Register your models here.
admin.site.register(verify_number)
admin.site.register(MakeCall)