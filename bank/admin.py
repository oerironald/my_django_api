# bank/admin.py
from django.contrib import admin
from .models import User, Account, Transaction, Loan

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Loan)