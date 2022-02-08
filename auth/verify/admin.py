from django.contrib import admin
from .models import UserInfo, MakeCall, UserCalls

# Register your models here.
class callsAdmin(admin.ModelAdmin):
    fields =  ['user', 'out_number', 'verify_number', 'call_date', 'coast']
    list_display = ('user', 'out_number', 'verify_number', 'call_date', 'coast')
    list_filter = ['user']


class UserInfoAdmin(admin.ModelAdmin):
    fields = ['user', 'url', 'calls_remaining', 'balance', 'coast_call', 'exp']
    list_display = ('user', 'url', 'calls_remaining', 'balance', 'coast_call', 'exp')

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(MakeCall)
admin.site.register(UserCalls, callsAdmin)