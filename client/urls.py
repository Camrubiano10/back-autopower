from .views import ClientViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r"client", ClientViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("license_plate/", include(router.urls))
]
