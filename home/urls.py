from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register(r'sliders', SliderViewSet, basename="sliders")
router.register(r'main', MainViewSet, basename="main")
router.register(r'service-sections', ServiceSectionViewSet, basename="service-sections")
router.register(r'services', ServiceViewSet, basename="services")
# router.register(r'abouts', AboutViewSet, basename="abouts")
# router.register(r'aboutus-contents', AboutUsContentsViewSet, basename="aboutus-contents")
router.register(r'news', NewsArticleViewSet, basename="news")


urlpatterns = [
    path('', include(router.urls)),
]