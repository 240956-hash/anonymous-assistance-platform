from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("support/", views.support, name="support"),
]
