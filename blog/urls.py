from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

# router.register(r'blogs', BlogPostViewSet, basename='blogs')
router.register(r'blogs', BlogViewSet, basename='blogs')

urlpatterns = [
    path('', include(router.urls)),
]