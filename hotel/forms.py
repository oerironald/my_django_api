from django import forms
from .models import Hotel, Room, Booking

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'