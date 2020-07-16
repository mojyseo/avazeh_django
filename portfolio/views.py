from django.shortcuts import render
from django.http import HttpResponse
from .models import Project 

# Create your views here.

def home(req):
    projects = Project.objects.all()
    return render(req, 'portfolio/home.html', {'projects': projects})
