from re import A
from django.contrib import admin
from .models import verify_number, MakeCall, calls

# Register your models here.
class callsAdmin(admin.ModelAdmin):
    fields =  ['user', 'out_number', 'verify_number', 'call_date']
    list_display = ('user', 'out_number', 'verify_number', 'call_date')
    list_filter = ['user']

admin.site.register(verify_number)
admin.site.register(MakeCall)
admin.site.register(calls, callsAdmin)