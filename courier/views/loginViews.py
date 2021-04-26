from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect("/login")

    else:
        return render(request, "pages/login.html")


def user_logout(request):
    logout(request)
    return redirect("/login")
