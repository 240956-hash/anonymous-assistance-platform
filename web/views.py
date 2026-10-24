from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET

@require_GET
def home(request):
    return render(request, "web/home.html")

@require_GET
def support(request):
    return render(request, "web/support.html")

@never_cache
@require_GET
def request_page(request):
    return render(request, "web/request.html")

@never_cache
@require_GET
def specialist_placeholder(request):
    return render(request, "web/specialist.html")
