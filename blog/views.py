from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def posts(request):
    return render(request, "post.html")

def explore(request):
    return render(request, "explore.html")

def single_post(request):
    pass
    