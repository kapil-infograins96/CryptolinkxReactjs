from django.urls import path
from .views import ExchangeViewAPI, WalletAPi

urlpatterns = [
  
    path('exchange/', ExchangeViewAPI.as_view(), name = 'exchange'),
    path('wallet_details/',WalletAPi.as_view(), name= 'wallet-details')
    

]