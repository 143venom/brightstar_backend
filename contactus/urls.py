from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'contact-background-image',ContactBackgroundImageViewSet, basename='contact-background-image')
router.register(r'contact-first-content',ContactFirstContentViewSet, basename='contact-first-content')
router.register(r'contact-second-content',ContactSecondContentViewSet, basename='contact-second-content')
router.register(r'contact-form',ContactFromViewSet, basename='contact-form')
router.register(r'contact-us-info',ContactUsInfoViewSet, basename='contact-us-info')
urlpatterns = [
    path("", include(router.urls)),
]