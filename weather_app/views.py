import requests
from django.shortcuts import render
from django.conf import settings

def weather_view(request):
    city = request.GET.get('city', 'New York')
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPEN_WEATHER_API_KEY}&units=metric'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        weather_data = None
        error_message = str(e)

    context = {
        'weather_data': weather_data,
        'error_message': error_message,
    }
    return render(request, 'weather_app/weather.html', context)