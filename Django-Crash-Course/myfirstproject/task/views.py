from django import forms
from django.http import HttpResponse
from django.shortcuts import render

list=["boss", "gauner", "gangster"]

def index(request):
    return render(request, "hello/index.html", {
        "tasks": list
    })

def add(request):
    return render(request, "hello/add.html")

def yes(request):
    return render(request, "hello/yes.html")

def brian(request):
    return HttpResponse("Hello, Brian.")

def calc(request):
    for x in range(1, 8):
        return HttpResponse("We are on time %d" % (x))
    
def horst(request):
    return HttpResponse("Hallo Horst")

def greet(request, names):
    return render(request, "hello/greet.html", {
        "namess": names.capitalize()
    })
