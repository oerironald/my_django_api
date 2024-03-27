import os
import re
import PyPDF2
from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_api.settings import BASE_DIR
from .access_token import generate_access_token
from .utils import timestamp_conversion
from .encode_base64 import generate_password
import requests
import json
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
import pandas as pd
from pdfminer.high_level import extract_text
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from PyPDF2 import PdfReader


# Create your views here.


# @api_view(['GET'])
# def get(request):

#         access_token = generate_access_token()
#         formated_time = timestamp_conversion()
#         decoded_password = generate_password(formated_time)

#         return Response({"access_token": access_token, "password": decoded_password})



# @api_view(['POST'])
# def make_payment(request, *args, **kwargs):
#         requestData = request.data
#         amount = requestData["amount"]
#         phone = requestData["phone_number"]

#         paymentResponseData =  make_mpesa_payment_request(amount= amount, phone= phone)

        # return Response(paymentResponseData)

# def make_mpesa_payment_request(amount: str, phone: str) -> dict:
#     access_token = generate_access_token()excel_files
#     formated_time = timestamp_conversion()
#     decoded_password = generate_password(formated_time)

#     headers = {"Authorization": "Bearer %s" % access_token}

#     request = {
#         "BusinessShortCode": settings.BUSINESS_SHORT_CODE,
#         "Password": decoded_password,'/workspaces/my_django_api/Documents/BG-From 14-9-23'
#         "Timestamp": formated_time,
#         "TransactionType": settings.TRANSACTION_TYPE,
#         "Amount": amount,
#         "PartyA": phone,
#         "PartyB": settings.BUSINESS_SHORT_CODE,
#         "PhoneNumber": phone,
#         "CallBackURL": settings.CALL_BACK_URL,
#         "AccountReference": settings.ACCOUNT_REFFERENCE,
#         "TransactionDesc": settings.TRANSACTION_DESCRIPTION
#     }

#     response = requests.post(settings.API_RESOURCE_URL, json=request, headers=headers)

#     try:
#         obbstr = response.json()
#     except json.JSONDecodeError:
#         # Handle JSON parsing error if necessary
#         obbstr = {}

#     merchant_request_id = obbstr.get('MerchantRequestID')
#     checkout_request_id = obbstr.get('CheckoutRequestID')
#     response_description = obbstr.get('ResponseDescription')
#     response_code = obbstr.get('Reget_access_token()sponseCode')

#     data = {
#         "merchant_request_id": merchant_request_id,
#         "checkout_request_id": checkout_request_id,
#         "response_description": response_description,
#         "response_code": response_code
#     }

#     return data

        


# def index(request, phone_number, amount):
#     cl = MpesaClient()
#     # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    
#     account_reference = 'reference'
#     transaction_desc = 'Description'
#     callback_url = 'https://ominous-system-wg6x6w4vjjpfgr59-8000.app.github.de'
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)


# def stk_push_callback(request):
#         data = request.body
        
#         #return HttpResponse("STK Push in Django👋")
#         return HttpResponse(data)




def payment_form(request):
    return render(request, 'daraja_api/index.html')

def process_payment(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = int(request.POST.get('amount'))  # Convert amount to an integer

        cl = MpesaClient()
        account_reference = 'Jogoo Oeri'
        transaction_desc = 'Payments'
        callback_url = 'https://ominous-system-wg6x6w4vjjpfgr59-8000.app.github.dev'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)

        return HttpResponseBadRequest("Invalid request method")
        


def extract_fields_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()

    # Process the extracted text to extract the desired fields
    lines = text.split('\n')
    fields = []
    for line in lines:
        if line.startswith('G02'):
            fields = line.split()
            break

    if len(fields) == 9:
        specimens = fields[0]
        position = fields[1]
        sample_id = fields[2]
        result_1 = fields[3]
        result_2 = fields[4]
        result_3 = fields[5]
        flags = fields[6]
        accepted_by = fields[7]

        return {
            'specimens': specimens,
            'position': position,
            'sample_id': sample_id,
            'result_1': result_1,
            'result_2': result_2,
            'result_3': result_3,
            'flags': flags,
            'accepted_by': accepted_by
        }
    else:
        return None

def extract_fields(request):
    if request.method == 'POST':
        pdf_folder = os.path.join(BASE_DIR, 'pdf_folder', 'BG')  # Replace with the actual path to your PDF folder

        fields = set()
        for filename in os.listdir(pdf_folder):
            if filename.endswith(".pdf"):
                filepath = os.path.join(pdf_folder, filename)
                extracted_fields = extract_fields_from_pdf(filepath)
                if extracted_fields is not None:
                    fields.update(extracted_fields)

        if fields:
            # Save the fields to an Excel file
            df = pd.DataFrame({'Fields': list(fields)})

            excel_folder = os.path.join(BASE_DIR, 'excel_files')  # Replace with the path to the desired folder to store the Excel file
            os.makedirs(excel_folder, exist_ok=True)  # Create the folder if it doesn't exist
            excel_filepath = os.path.join(excel_folder, 'excel_file.xlsx')  # Replace with the desired filename for the Excel file

            # Create a new workbook using openpyxl
            workbook = Workbook()
            worksheet = workbook.active

            # Write the DataFrame to the worksheet
            for row in dataframe_to_rows(df, index=False, header=True):
                worksheet.append(row)

            # Save the workbook
            workbook.save(excel_filepath)

            return render(request, 'daraja_api/results.html', {'excel_filepath': excel_filepath})
        else:
            return render(request, 'daraja_api/no_results.html')

    return render(request, 'daraja_api/extract.html')