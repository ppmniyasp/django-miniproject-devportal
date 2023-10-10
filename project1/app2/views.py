from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def taskhome(request):
    return HttpResponse("<h1> hello from task/home page </h1>")

def taskabout(request):
    return HttpResponse("<h1> hello from task/about page </h1>")
