from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    event.preventDefault()

def get_article(request, article_name):
    return render(request, f'{article_name}.html')

