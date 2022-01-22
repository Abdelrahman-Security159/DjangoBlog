from django.shortcuts import render
from .forms import LoginForm, RegForm


def register(request):
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            return render(request, "done.html")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form":form})

def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, "done.html")
    else:
        form = RegForm()
    return render(request, "register.html", {"form":form})