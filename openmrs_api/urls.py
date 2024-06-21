from django.urls import path
from .views import get_patients, search_patients

urlpatterns = [
    path('', get_patients, name='patient_list'),
    path('search/', search_patients, name='search_patients'),
]
