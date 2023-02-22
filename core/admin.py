from django.contrib import admin
from core.models import Currency, Wallet, Order


# Register your models here.

class WalletAdmin(admin.ModelAdmin):
    model = Wallet
    list_display = ['user','money','Currency_type']



class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['user','status','time']

admin.site.register(Currency)
admin.site.register(Wallet, WalletAdmin)

admin.site.register(Order, OrderAdmin)
