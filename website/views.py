from django.shortcuts import render
from .models import Art

def home(request):
    arts = Art.objects.all()
    return render(request, "home.html", {'arts': arts})
