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


# Chose = (
#     ('Buy','Buy'),
#     ('Sell','Sell')
# )

# class Crypto_Wallets(models.Model):
#     user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
#     type = models.CharField(max_length = 20, choices = Chose ,default = 'Buy')
#     crypto_name = models.CharField(max_length=50)
#     crypto_price = models.FloatField()
#     quantity = models.FloatField()
#     invested_rs = models.FloatField()

#     class Meta:
#         verbose_name = 'Crypto_Wallet'

#     def __str__(self):
#         return self.user.email
        
        
Order_chose = (
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Cancel','Cancel')
)

Chose = (
     ('Buy','Buy'),
     ('Sell','Sell')
 )

class Order(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    type = models.CharField(max_length = 20, choices = Chose ,default = 'Buy')
    crypto_name = models.CharField(max_length=50)
    crypto_price = models.FloatField()
    quantity = models.FloatField()
    invested_rs = models.FloatField()
    fee = models.FloatField()
    status = models.CharField(max_length=50,choices=Order_chose,default='Cancel')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.crypto_name} - {self.user}'
    

    
class Crypto_wallet(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE,null=True)
    crypto_name = models.CharField(max_length=50,null=True,blank=True)
    quantity = models.FloatField()
    invested = models.FloatField() 

    def __str__(self):
        return f'{self.order}'
    

   
    






    
