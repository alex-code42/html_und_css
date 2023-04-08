from django.http import HttpResponse

from django.shortcuts import render

list = ["laufen","schlafen", "essen"]

def aufgabe(request):
    return render(request, "aufgabe/index.html")