from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Custom_User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length = 100, unique = True, blank = False, null  = False)
    phone = models.CharField(max_length = 17, blank = True)
    username = models.CharField(max_length = 20, blank= True)
    first_name = models.CharField(max_length= 20, blank= True)
    middle_name = models.CharField(max_length = 100, blank = True)
    last_name = models.CharField(max_length= 20, blank= True)
    password = models.CharField(max_length = 200, blank= True)
    dob = models.DateField(null = True, blank = True)
    city = models.CharField(max_length= 20, blank= True)
    state = models.CharField(max_length= 20, blank= True)
    zipcode = models.CharField(max_length = 10, blank = True)
    address = models.CharField(max_length= 80, blank= True)
    country = models.CharField(max_length= 20, blank= True)
    is_otp_verified = models.BooleanField(default = False)
    is_kyc_verified = models.BooleanField(default = False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects =  CustomUserManager()

    def __str__(self):
        return self.email
