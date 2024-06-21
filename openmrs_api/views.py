import requests
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientSearchForm



def get_patients(request):
    url = "https://demo.openmrs.org/openmrs/ws/rest/v1/patient"
    params = {
        'q': '',  # Adjust this if needed
        'limit': 100,
        'startIndex': 0
    }
    response = requests.get(url, params=params, auth=('admin', 'Admin123'))
    
    if response.status_code == 200:
        patients = response.json().get('results', [])
        if not patients:
            print("No patients found.")
        else:
            print("Patients found:", patients)
        return render(request, 'openmrs_api/patient_list.html', {'patients': patients})
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return HttpResponse(f"Error: {response.status_code} - {response.text}")


def search_patients(request):
    if request.method == 'GET':
        form = PatientSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query', '')

            url = "https://demo.openmrs.org/openmrs/ws/rest/v1/patient"
            params = {
                'q': search_query,
                'limit': 100,
                'startIndex': 0
            }

            response = requests.get(url, params=params, auth=('admin', 'Admin1234'))

            if response.status_code == 200:
                patients = response.json().get('results', [])
                if not patients:
                    print("No patients found.")
                else:
                    print("Patients found:", patients)
                return render(request, 'openmrs_api/search_patients.html', {'patients': patients, 'form': form})
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return HttpResponse(f"Error: {response.status_code} - {response.text}")

    else:
        form = PatientSearchForm()

    return render(request, 'openmrs_api/search_patients.html', {'form': form})