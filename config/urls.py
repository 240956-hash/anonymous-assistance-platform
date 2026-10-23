from django.urls import path
from core.views import health

urlpatterns = [path("api/health/", health, name="health")]
