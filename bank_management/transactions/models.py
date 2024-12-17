from django.db import models
from accounts.models import UserBankAccount
from .constants import TRANSACTION_TYPE

# Create your models here.
class Transactions(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']