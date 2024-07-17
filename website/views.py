from django.shortcuts import render, redirect
from .models import Art
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    arts = Art.objects.all()
    return render(request, "home.html", {'arts': arts})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username, password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Zalogowano poprawnie...')
            return redirect('home')
        else:
            messages.success(request, 'Wystąpił błąd w trakcie logowania. Spróbuj ponownie...')
            return redirect('login_user')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Wylogowano poprawnie...")
    return redirect('home')