from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def blast(request):
    return render(request, "pages/blast.html")

def faceit(request):
    return render(request, "pages/faceit.html")

def hltv(request):
    return render(request, "pages/hltv.html")




