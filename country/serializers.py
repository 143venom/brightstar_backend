from rest_framework import serializers
from .models import *


class CountrysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ["created_at", "updated_at"]


class CountryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInfo
        exclude = ["created_at", "updated_at"]


class CountrySubmitInitialDucumentsContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountrySubmitInitialDucumentsContent
        exclude = ["created_at", "updated_at"]


class CountrySubmitInitialDucumentsSerializer(serializers.ModelSerializer):
    countrysubmitinitialducumentscontent = (
        CountrySubmitInitialDucumentsContentSerializer(
            many=True, source="countrysubmitinitialducumentscontent_set"
        ),
    )

    class Meta:
        model = CountrySubmitInitialDucuments
        exclude = ["created_at", "updated_at"]


class CountryInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryInterview
        exclude = ["created_at", "updated_at"]


class CountryIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryIdentity
        exclude = ["created_at", "updated_at"]


class CountryOfferLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryOfferLetter
        exclude = ["created_at", "updated_at"]


class CountryEmbassyAppointmentContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryEmbassyAppointmentContent
        exclude = ["created_at", "updated_at"]


class CountryEmbassyAppointmentSerializer(serializers.ModelSerializer):
    countryembassyapointmentcontent = CountryEmbassyAppointmentContentSerializer(
        many=True, source="countryembassyappointmentcontent_set"
    )

    class Meta:
        model = CountryEmbassyAppointment
        exclude = ["created_at", "updated_at"]


class CountrySerializer(serializers.ModelSerializer):
    countryinfo = CountryInfoSerializer(many=True, source="countryinfo_set")
    countrysubmitinitialducuments = CountrySubmitInitialDucumentsSerializer(
        many=True, source="countrysubmitinitialducuments_set"
    )
    countryinterview = CountryInterviewSerializer(
        many=True, source="countryinterview_set"
    )
    countryidentity = CountryIdentitySerializer(many=True, source="countryidentity_set")
    countryofferletter = CountryOfferLetterSerializer(
        many=True, source="countryofferletter_set"
    )
    countryembassyappointment = CountryEmbassyAppointmentSerializer(
        many=True, source="countryembassyappointment_set"
    )

    class Meta:
        model = Country
        exclude = ["created_at", "updated_at"]
