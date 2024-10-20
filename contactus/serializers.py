from .models import *
from rest_framework import serializers


class ContactBackgroundImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactBackgroundImage
        fields = "__all__"


class ContactFirstContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFirstContent
        fields = "__all__"


class ContactSecondContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSecondContents
        fields = "__all__"


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"


class ContactUsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsInfo
        fields = "__all__"
