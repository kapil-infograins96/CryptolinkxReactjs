from django.contrib import admin
from core.models import Currency, Wallet


# Register your models here.

class WalletAdmin(admin.ModelAdmin):
    model = Wallet
    list_display = ['user','money','Currency_type']

admin.site.register(Currency)
admin.site.register(Wallet, WalletAdmin)