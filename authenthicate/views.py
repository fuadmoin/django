from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'authenticate/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Login Error'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('Logged Out'))
    return redirect('login')

def register_user(request):
    return render(request, 'authenticate/userRegister.html', {})


def register_restaurant(request):
    return render(request, 'authenticate/cafeRegister.html', {})




