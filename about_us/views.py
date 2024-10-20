from rest_framework import viewsets
from .models import *
from .serializers import *


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class AboutUsContentImageViewSet(viewsets.ModelViewSet):
    queryset = AboutUsContentImage.objects.all()
    serializer_class = AboutUsContentImageSerializer


class AboutUsContentsViewSet(viewsets.ModelViewSet):
    queryset = AboutUsContents.objects.all()
    serializer_class = AboutUsContentsSerializer
