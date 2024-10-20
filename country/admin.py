from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(CountryInfo)
admin.site.register(CountrySubmitInitialDucuments)
admin.site.register(CountrySubmitInitialDucumentsContent)
admin.site.register(CountryInterview)
admin.site.register(CountryIdentity)
admin.site.register(CountryOfferLetter)
admin.site.register(CountryEmbassyAppointment)
admin.site.register(CountryEmbassyAppointmentContent)
