from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .access_token import generate_access_token
from .utils import timestamp_conversion
from .encode_base64 import generate_password
import requests
import json
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse

# Create your views here.


@api_view(['GET'])
def get(request):

        access_token = generate_access_token()
        formated_time = timestamp_conversion()
        decoded_password = generate_password(formated_time)

        return Response({"access_token": access_token, "password": decoded_password})



@api_view(['POST'])
def make_payment(request, *args, **kwargs):
        requestData = request.data
        amount = requestData["amount"]
        phone = requestData["phone_number"]

        paymentResponseData =  make_mpesa_payment_request(amount= amount, phone= phone)

        return Response(paymentResponseData)

def make_mpesa_payment_request(amount: str, phone: str) -> dict:
    access_token = generate_access_token()
    formated_time = timestamp_conversion()
    decoded_password = generate_password(formated_time)

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": settings.BUSINESS_SHORT_CODE,
        "Password": decoded_password,
        "Timestamp": formated_time,
        "TransactionType": settings.TRANSACTION_TYPE,
        "Amount": amount,
        "PartyA": phone,
        "PartyB": settings.BUSINESS_SHORT_CODE,
        "PhoneNumber": phone,
        "CallBackURL": settings.CALL_BACK_URL,
        "AccountReference": settings.ACCOUNT_REFFERENCE,
        "TransactionDesc": settings.TRANSACTION_DESCRIPTION
    }

    response = requests.post(settings.API_RESOURCE_URL, json=request, headers=headers)

    try:
        obbstr = response.json()
    except json.JSONDecodeError:
        # Handle JSON parsing error if necessary
        obbstr = {}

    merchant_request_id = obbstr.get('MerchantRequestID')
    checkout_request_id = obbstr.get('CheckoutRequestID')
    response_description = obbstr.get('ResponseDescription')
    response_code = obbstr.get('ResponseCode')

    data = {
        "merchant_request_id": merchant_request_id,
        "checkout_request_id": checkout_request_id,
        "response_description": response_description,
        "response_code": response_code
    }

    return data

        


def index(request, phone_number, amount):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://ominous-system-wg6x6w4vjjpfgr59-8000.app.github.de'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


def stk_push_callback(request):
        data = request.body
        
        #return HttpResponse("STK Push in Django👋")
        return HttpResponse(data)




def payment_form(request):
    return render(request, 'daraja_api/index.html')

def process_payment(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = int(request.POST.get('amount'))  # Convert amount to an integer

        cl = MpesaClient()
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://ominous-system-wg6x6w4vjjpfgr59-8000.app.github.de'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)

        return HttpResponseBadRequest("Invalid request method")