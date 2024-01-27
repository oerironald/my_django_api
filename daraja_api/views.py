from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .access_token import generate_access_token
from .utils import timestamp_conversion
from .encode_base64 import generate_password
import requests
import json

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


def make_mpesa_payment_request(amount: str, phone: str)->dict:
        access_token = generate_access_token()
        formated_time = timestamp_conversion()
        decoded_password = generate_password(formated_time)

        headers = {"Authorization": "Bearer %s" % access_token}

        request = {
                "BusinessShortCode": settings.BUSINESS_SHORT_CODE,   
                "Password": decoded_password,   
                "Timestamp":formated_time,   
                "TransactionType": settings.TRANSACTION_TYPE,    
                "Amount": amount,    
                "PartyA":phone,    
                "PartyB":settings.BUSINESS_SHORT_CODE,    
                "PhoneNumber":phone,    
                "CallBackURL": settings.CALL_BACK_URL,    
                "AccountReference":settings.ACCOUNT_REFFERENCE,    
                "TransactionDesc":settings.TRANSACTION_DESCRIPTION
        }

        response = requests.post(settings.API_RESOURCE_URL, json=request, headers=headers)

        mystr = response.text
        obbstr = json.loads(mystr)


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


        