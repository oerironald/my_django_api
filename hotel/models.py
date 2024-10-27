from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

class BookingDetail(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    service_description = models.CharField(max_length=255)

class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class RoomServices(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)