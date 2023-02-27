from rest_framework import serializers
from core.models import Wallet, Order, Crypto_wallet




class WalletSerializer(serializers.ModelSerializer):
    Currency_type = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Wallet
        fields = ['user','money','Currency_type']

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class CryptoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Crypto_wallet
        fields = "__all__"

        

