from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"jobs", JobsViewSet, basename="jobs")
router.register(r"job-application", JobApplicationViewSet, basename="job-application")

urlpatterns = [
    path("", include(router.urls)),
]
