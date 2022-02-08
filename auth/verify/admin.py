from django.contrib import admin
from .models import UserInfo, MakeCall, UserCalls

# Register your models here.
class callsAdmin(admin.ModelAdmin):
    fields =  ['user', 'out_number', 'verify_number', 'call_date']
    list_display = ('user', 'out_number', 'verify_number', 'call_date')
    list_filter = ['user']

admin.site.register(UserInfo)
admin.site.register(MakeCall)
admin.site.register(UserCalls, callsAdmin)