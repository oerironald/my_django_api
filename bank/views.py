# bank/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from rest_framework import viewsets

from .models import Account, Transaction, Loan
from .serializers import AccountSerializer, TransactionSerializer, LoanSerializer
from .forms import AccountForm

@login_required
def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'bank/account_detail.html', {'account': account})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('account_list')  # replace 'home' with your desired redirect URL name

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'bank/account_list.html'
    context_object_name = 'accounts'

class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'bank/account_detail.html'
    context_object_name = 'account'

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'bank/account_form.html'
    success_url = reverse_lazy('bank:account_list')

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'bank/account_form.html'
    success_url = reverse_lazy('bank:account_list')

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'bank/account_confirm_delete.html'
    success_url = reverse_lazy('bank:account_list')