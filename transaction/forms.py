from django import forms
from .models import Transaction


class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']
    

    # user er account ta ekhane pass kore dibo
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') # (views theke) account value ke pop kore anlam

        super().__init__(*args, **kwargs)

    
    # function to save transaction activity
    def save(self, commit=True):
        self.instance.account = self.account # current account object hishebe ektu age __init__ function theke capture kora account ke ekhane die dibo 

        self.instance.balance_after_transaction = self.account.balance  # kono transaction (eg: deposit) hober pore sei new amount balance die tar account er balance_after_transaction ke update kore dicchi

        return super().save() # finally, parent ke overwrite kore tar account and updated balance save kore dicchi
    


    def clean_amount(self): # amount field ke filter korbo
        min_deposit_amount = 100

        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam

        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount
    
