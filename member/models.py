from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE


# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True) # different user er bank account number alada alada hobe, kokhono ek hobe na..

    contact_no = models.CharField(max_length=11)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)

    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) # ekjon user 12 digit porjonto taka rakhte parbe, dui doshomik vabe o rakhte parbe. for example: 1000.50


    def __str__(self):
        return f'{self.account_no} - {self.user}'
    




class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)

    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)


    def __str__(self):
        return f'Address of {self.user.account.user.username}: {self.city}, {self.postal_code}, {self.country}'



