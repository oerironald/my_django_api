# bank/forms.py
from django import forms
from .models import Account, Transaction, Loan

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user', 'balance', 'account_number']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'transaction_type']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['account', 'amount', 'interest_rate']