from django.db import models
from account.models import Custom_User

# Create your models here.


class Currency(models.Model):
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.currency


class Wallet(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    money = models.FloatField()
    Currency_type = models.ForeignKey(Currency, on_delete=models.CASCADE)

    
