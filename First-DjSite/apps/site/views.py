from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    event.preventDefault()

def Faceit(request):
    return render(request, "Faceit.html")
    event.preventDefault()

def blast(request):
    return render(request, "blast.html")
    event.preventDefault()

def hltv(request):
    return render(request, "hltv.html")
    event.preventDefault()

