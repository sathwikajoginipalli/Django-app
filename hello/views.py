from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def Sathwi(request):
    return HttpResponse("Hello Sathwika!")

def dhatri(request):
    return HttpResponse("Hello Dhatri!")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })