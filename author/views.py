from django.shortcuts import render
from .forms import LoginForm, RegForm
from .models import Author


author = ['username', 'firstname', 'lastname', 'email', 'password', 'age', 'avatar']

def user_exists(username):
    try:
        Author.objects.get(user_name=username)
        return True
    except Author.DoesNotExist:
        return False

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            valid = user_exists(username)
            if valid:
                validated_user = Author.objects.get(user_name=username)
                if username:
                    if validated_user.password == password:
                        return render(request, "done.html")

    form = LoginForm()
    return render(request, "login.html", {"form":form})

def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        
        if form.is_valid():
            for i in range(5):
                author[i] = form.cleaned_data[author[i]]
            
            return render(request, "upload.html")
    else:
        form = RegForm()
    return render(request, "register.html", {"form":form})

def upload(request):
    if request.method == "POST":
        image = request.FILES['avatar']
        author[6] = image
        account = Author(
            user_name=author[0],
            first_name=author[1],
            last_name=author[2],
            email=author[3],
            password=author[4],
            age=0,
            avatar=image
            )
        account.save()
        form = LoginForm()
        return render(request, "login.html", {"form":form})
