from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django_daraja.mpesa.core import MpesaClient


def payment_form(request):
    return render(request, 'daraja_api/index.html')

def process_payment(request, phone_number, amount):
    if request.method == 'POST':
        try:
            amount = int(amount)  # Convert amount to an integer

            cl = MpesaClient()
            account_reference = 'Jogoo Oeri'
            transaction_desc = 'Payments'
            callback_url = 'https://example.com/callback/'  # Replace with your callback URL
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            return HttpResponse(response)
        except ValueError:
            return HttpResponseBadRequest("Invalid amount format")

    return HttpResponseBadRequest("Invalid request method")