from django.urls import path
from .views import covid_data_view, country_data_view

urlpatterns = [
    path('', covid_data_view, name='covid_data'),
    path('country/', country_data_view, name='country'),
]
