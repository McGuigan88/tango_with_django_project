from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href = '/rango/about/'>About</a> Rango says hey there partner!")

def about(request):
    return HttpResponse("<a href = '/rango/index/'>index</a>Rango says here is the about page")