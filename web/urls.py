from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("support/", views.support, name="support"),
    path("request/", views.request_page, name="request-page"),
]
