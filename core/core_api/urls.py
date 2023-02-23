from django.urls import path
from .views import ExchangeViewAPI, WalletAPi,Buy_CryptoAPI,Sell_CryptoAPI

urlpatterns = [
  
    path('exchange/', ExchangeViewAPI.as_view(), name = 'exchange'),
    path('wallet_details/',WalletAPi.as_view(), name= 'wallet-details'),
    path('buy_crypto/',Buy_CryptoAPI.as_view(), name = 'buy-crypto'),
    path('sell_crypto/',Sell_CryptoAPI.as_view(),name= 'sell-crypto')

]