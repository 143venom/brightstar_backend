from django.db import models
from core.models import BaseModel


# Create your models here.
class Country(BaseModel):
    country = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.country


class CountryInfo(BaseModel):
    image = models.ImageField(upload_to="images/country/")
    title_1 = models.CharField(max_length=255)
    title_2 = models.CharField(max_length=255)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_1


class CountrySubmitInitialDucuments(BaseModel):
    image = models.ImageField(upload_to="images/country/")
    title = models.CharField(max_length=255, default="need to change title")
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CountrySubmitInitialDucumentsContent(BaseModel):
    title = models.CharField(max_length=255, default="need to change title")
    countrysubmitinitialdocument = models.ForeignKey(
        CountrySubmitInitialDucuments, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class CountryInterview(BaseModel):
    title = models.CharField(max_length=255, default="need to change title")
    image = models.ImageField(upload_to="images/country/")
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class CountryIdentity(BaseModel):
    title = models.CharField(max_length=255, default="need to change title")
    image = models.ImageField(upload_to="images/country/")
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class CountryOfferLetter(BaseModel):
    title = models.CharField(max_length=255, default="need to change title")
    image = models.ImageField(upload_to="images/country/")
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class CountryEmbassyAppointment(BaseModel):
    title = models.CharField(max_length=255, default="need to change title")
    image = models.ImageField(upload_to="images/country/")
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class CountryEmbassyAppointmentContent(BaseModel):
    title = models.CharField(max_length=255, default="need to change title")
    countryembassyappointment = models.ForeignKey(
        CountryEmbassyAppointment, on_delete=models.CASCADE
    )
