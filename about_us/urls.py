from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register(r'about-us', AboutUsViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'about-us-content-image', AboutUsContentImageViewSet, basename="about-us-content-image")
router.register(r'about-us-contents', AboutUsContentsViewSet, basename="about-us-contents")


urlpatterns = [
    path('', include(router.urls)),
]