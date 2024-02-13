from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.


def user_login(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        id = request.POST["username"]
        pw = request.POST["password"]
        user = authenticate(username=id, password=pw)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("post-list")
        else:
            return redirect("user-login")
    else:
        form = LoginForm()
        return render(request, "users/account_login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("post-list")
