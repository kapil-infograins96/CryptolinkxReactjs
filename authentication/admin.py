from django.contrib import admin
from authentication.models import Email_OTP, KYC

# Register your models here.




class OTP_Admin(admin.ModelAdmin):
   
    list_display = ['email', 'otp']

class KYCAdmin(admin.ModelAdmin):
    
    list_display = ['id_number','user'] 


admin.site.register(KYC, KYCAdmin)
admin.site.register(Email_OTP, OTP_Admin)
