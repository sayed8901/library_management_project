from django.db import models
from member.models import UserAccount


# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, related_name='transactions', on_delete=models.CASCADE)     # ekjon user er multiple transactions hote pare

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['timestamp',]   # sorting transactions data by timestamp
    

    def __str__(self):
        return f"{self.account.user.username} deposited: {self.amount}"

