from django.contrib import admin
from . models import(TravelTour,BlogPost,EmbassyBooking,AirlineTicketReservation,
                     HotelBooking,PassportVisaConsultation,CarHire)

admin.site.register(TravelTour)
admin.site.register(EmbassyBooking)
admin.site.register(AirlineTicketReservation)
admin.site.register(HotelBooking)
admin.site.register(PassportVisaConsultation)
admin.site.register(CarHire)
admin.site.register(BlogPost)


