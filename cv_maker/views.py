from rest_framework import viewsets
from .models import CV
from rest_framework.response import Response
from rest_framework import status
from .serializers import CVSerializer


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
