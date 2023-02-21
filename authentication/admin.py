from django.contrib import admin
from authentication.models import KYC, Email_OTP

# Register your models here.

admin.site.register(KYC)
admin.site.register(Email_OTP)
