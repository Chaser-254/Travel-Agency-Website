from django.db import models
from django.contrib.auth.models import User

class TravelTour(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class EmbassyBooking(models.Model):
    embassy_name = models.CharField(max_length=200)
    booking_date = models.DateField()
    preparation_notes = models.TextField()

class AirlineTicketReservation(models.Model):
    airline_name = models.CharField(max_length=200)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    destination = models.CharField(max_length=200)

class PassportVisaConsultation(models.Model):
    consultation_date = models.DateField()
    consultation_notes = models.TextField()

class CarHire(models.Model):
    car_model = models.CharField(max_length=200)
    hire_start_date = models.DateField()
    hire_end_date = models.DateField()

class HotelBooking(models.Model):
    hotel_name = models.CharField(max_length=200)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    travel_tour = models.ForeignKey(TravelTour, on_delete=models.CASCADE)

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)