from django.shortcuts import render
from .forms import TestForm


def register(request):
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        
        if form.is_valid():
            return render(request, "done.html")
    else:
        form = TestForm()
    return render(request, "login.html", {"form":form})

def test(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, "done.html")
    else:
        form = TestForm()
    return render(request, "test.html", {"form":form})