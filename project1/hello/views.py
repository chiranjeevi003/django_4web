import re
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html") # to render an html file > return render(request, "hello/index.html")

def chp5(request):
    return HttpResponse("Hello, Chiru")

def harshu(request):
    return HttpResponse("Hello, Harshitha")


def  greet(request, name):
    return render(request, "hello/greet.html",{
        "name":name.capitalize()
    })
