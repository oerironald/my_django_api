from django.shortcuts import render
from .api import get_covid_data, get_country_data

def covid_data_view(request):
    data = get_covid_data()
    return render(request, 'covid19/covid_data.html', {'data': data})


def country_data_view(request):
    # Get selected country from form input or default to empty string
    selected_country = request.GET.get('country', '')

    # If a country is selected, fetch its data
    country_data = None
    if selected_country:
        country_data = get_country_data(selected_country)

    return render(request, 'covid19/country_data.html', {'selected_country': selected_country, 'country_data': country_data})