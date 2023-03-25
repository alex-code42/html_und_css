from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return render(request, "hello/index.html")

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
