from rest_framework import viewsets
from .models import *
from .serializers import *


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class MainViewSet(viewsets.ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class ServiceSectionViewSet(viewsets.ModelViewSet):
    queryset = ServiceSection.objects.all()
    serializer_class = ServiceSectionSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# class AboutViewSet(viewsets.ModelViewSet):
#     queryset = AboutUsContentImage.objects.all()
#     serializer_class = AboutUsContentImageSerializer


# class AboutUsContentsViewSet(viewsets.ModelViewSet):
#     queryset = AboutUsContents.objects.all()
#     serializer_class = AboutUsContentsSerializer


class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
