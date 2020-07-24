from django.shortcuts import render
from django.http import HttpResponse
from .models import Project 

# Create your views here.

def home(req):
    projects = Project.objects.all()
    return render(req, 'portfolio/home.html', {'projects': projects})
def home_en(req):
    projects = Project.objects.all()
    return render(req, 'portfolio/home-en.html', {'projects': projects})


def about(req):
    return render(req, 'portfolio/about.html')
def about_en(req):
    return render(req, 'portfolio/about-en.html')


def products(req):
    return render(req, 'portfolio/products.html')
def products_en(req):
    return render(req, 'portfolio/products-en.html')


def contact(req):
    return render(req, 'portfolio/contact.html')
def contact_en(req):
    return render(req, 'portfolio/contact-en.html')
