from rest_framework import serializers
from core.models import Wallet




class WalletSerializer(serializers.ModelSerializer):
    Currency_type = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Wallet
        fields = ['user','money','Currency_type']

