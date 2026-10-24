from django.shortcuts import render
from django.views.decorators.http import require_GET

@require_GET
def home(request):
    return render(request, "web/home.html")

@require_GET
def support(request):
    return render(request, "web/support.html")
