from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User created successfully")
            return redirect("home")
        else:
            messages.error(request, 'an error happened during registration')
    context = {"form": form}
    return render(request, 'user/register.html', context)

def LoginUser(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email =  request.POST.get("email")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "invalid username")
        user = authenticate(request, username=username, password=password, email=email)
        if user is not None:
            login(request, user)
            messages.success(request, "welcome get confortable please")
            return redirect("home")
        else:
            messages.warning(request, "you got a null response")

    if request.user.is_authenticated:
        return HttpResponse("you are already logged in, Want to logout, head to the homepage and click login")
    context = {"page":page}
    return render(request, 'user/register.html', context)

def LogoutUser(request):
    logout(request)
    return redirect("home")