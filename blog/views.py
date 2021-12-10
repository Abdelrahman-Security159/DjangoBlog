from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")
    

def posts(request):
    pass

def single_post(request):
    pass
    