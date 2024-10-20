from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CVViewSet

router = DefaultRouter()
router.register(r"build-cv", CVViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
