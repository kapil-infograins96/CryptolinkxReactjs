from django.contrib import admin
from core.models import Currency, Wallet, Order, Crypto_wallet


# Register your models here.

class WalletAdmin(admin.ModelAdmin):
    model = Wallet
    list_display = ['user','money','Currency_type']

class Crypto_walletAdmin(admin.ModelAdmin):
    model =Crypto_wallet
    list_display  = ['order','quantity','invested']

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['user','status','time']



admin.site.register(Currency)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Crypto_wallet, Crypto_walletAdmin)
admin.site.register(Order, OrderAdmin)
