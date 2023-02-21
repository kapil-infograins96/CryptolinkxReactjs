from django.db import models
from account.models import Custom_User

# Create your models here.
DOC_TYPE = (
    ('SSN','SSN'),
    ('PASSPORT','PASSPORT'),
    ('DRIVING_LICENSE','DRIVING_LICENSE'),
)

class KYC(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length = 20, choices = DOC_TYPE ,default = 'SSN')
    id_number = models.IntegerField()
    doc_front_img  = models.ImageField(null = True, blank = True)
    doc_back_img = models.ImageField(null = True, blank = True) 
    doc_selfie = models.ImageField(null = True, blank = True)

    def __str__(self):
        return f'{self.id_number}-------->{self.user}'

class Email_OTP(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 50)
    otp = models.IntegerField()

    def __str__(self):
        return f'{self.email} with {self.otp}'



