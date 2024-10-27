from django.urls import path
from .views import hotel_list, create_hotel

app_name = 'hotel'

urlpatterns = [
    path('', hotel_list, name='hotel_list'),
    path('create/', create_hotel, name='create_hotel'),
]