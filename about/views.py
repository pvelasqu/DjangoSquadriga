from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def about(request):
    return render(request, 'about/about_team.html')


def pablo(request):
    return render(request, 'about/about_pablo.html')