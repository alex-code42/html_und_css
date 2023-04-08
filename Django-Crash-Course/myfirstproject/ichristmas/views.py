from django.shortcuts import render

from datetime import date

from django.http import HttpResponse

# Create your views here.

geburtstag = date(1986,4,19)
heute = date.today()
alter = heute - geburtstag

weihnachten2023 = date(2023, 12, 24)

if date.today() == weihnachten2023: 
    weihnachten = "JA"
else:
    weihnachten = "NEIN"


def date_today(request):
    context = {
        "date": date.today(),
        "auto": 'Mercedes',
        "alter": alter.days,
        "chr": weihnachten, 
    }
    return render(request, "ichristmas/date.html", context)