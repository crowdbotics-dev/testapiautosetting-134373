from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134373ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134373", Testconnectors134373ViewSet, basename="testconnectors134373"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
