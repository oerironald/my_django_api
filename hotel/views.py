from django.shortcuts import render, redirect
from .models import Hotel, Room, Booking
from .forms import HotelForm, RoomForm, BookingForm

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/hotel_list.html', {'hotels': hotels})

def create_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel:hotel_list')
    else:
        form = HotelForm()
    return render(request, 'hotel/hotel_form.html', {'form': form})