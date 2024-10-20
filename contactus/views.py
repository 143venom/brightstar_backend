from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets


# Create your views here.
class ContactBackgroundImageViewSet(viewsets.ModelViewSet):
    queryset = ContactBackgroundImage.objects.all().order_by("-id")
    serializer_class = ContactBackgroundImageSerializer


class ContactFirstContentViewSet(viewsets.ModelViewSet):
    queryset = ContactFirstContent.objects.all().order_by("-id")
    serializer_class = ContactFirstContentSerializer


class ContactSecondContentViewSet(viewsets.ModelViewSet):
    queryset = ContactSecondContents.objects.all().order_by("-id")
    serializer_class = ContactFirstContentSerializer


class ContactFromViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer


class ContactUsInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactUsInfo.objects.all()
    serializer_class = ContactUsInfoSerializer
