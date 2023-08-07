from django import forms
from .models import BlogPost,EmbassyBooking,TravelTour,AirlineTicketReservation

class BlogPostForm(forms.ModelForm):
    class Meta:
        fields = ('title','content')
        model = BlogPost

class EmbassyBookingForm(forms.ModelForm):
    class Meta:
        model = EmbassyBooking
        fields = ['embassy_name', 'booking_date', 'preparation_notes']

class AirlineTicketReservationForm(forms.ModelForm):
    class Meta:
        model = AirlineTicketReservation
        fields = ['airline_name', 'departure_date', 'arrival_date', 'destination']

class TravelTourForm(forms.ModelForm):
    class Meta:
        model = TravelTour
        fields = ['name', 'description', 'start_date', 'end_date']