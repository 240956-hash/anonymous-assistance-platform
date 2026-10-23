from django.urls import path
from core.views import health
from core.api import request_prototype

urlpatterns = [
    path("api/health/", health, name="health"),
    path("api/requests/", request_prototype, name="request-prototype"),
]
