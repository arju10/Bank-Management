from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER_TYPE

# Create user using django builtin facilities
class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE) 
    '''
    purpose of using parameter:
    1. related_name='account" means We can use access user information using 'account' name. One user has only one account.
    2. on_delete=models.CASCADE means If the user is deleted, this user related all data will be deleted.
    3. OneToOneField means Every single user is unique , and relation with other things like address, city etc. will not be more than one. It means, One user has one city.
    4. User -> It is Django builtin User
    '''
    account_type = models.CharField(max_length=10, choices= ACCOUNT_TYPE)
    '''
    5. choices=ACCOUNT_TYPE; It means user can select one option among many options.Here,There are Savings and Current type. User can select Savings or Current type account.
    '''
    account_no = models.IntegerField(unique=True) # Account number can't be duplicate, must be unique.
    birth_date = models.DateField(null=True, blank=True) # If user don't want to input the birthday date.
    gender = models.TextField(max_length=10, choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    '''
    1.  auto_now_add=True ; When user create a account, it will automatically create a date.
    '''
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    '''
    1. default:0; When User create a account by default his account balance will be showing 0
    2. max_digits=12; User can deposite or savings his balance not more than 12 digit like 100000000000
    3. decimal_places=2 ; Means Taka can be deposited 10.15tk not 10.156tk
    '''

    def __str__(self):
        return str(self.account_no)

class UserAddress(models.Model):
    user =  models.OneToOneField(User, related_name='address', on_delete= models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.email)