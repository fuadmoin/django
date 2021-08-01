from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserProfileForm,  CafeSignUpForm , CafeProfileForm


def home(request):
    return render(request, 'authenticate/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.email !="":
                return redirect('home')
            else:
                return redirect('uregister')
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile = UserProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            user = form.save()

            profile2 = profile.save(commit=False)
            profile2.user = user
            profile2.save()


            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()
        profile = UserProfileForm()
    context = {'form': form ,'profile': profile}
    return render(request, 'authenticate/userRegister.html', context)




    
def register_restaurant(request):
    if request.method == 'POST':
        form2 = CafeSignUpForm(request.POST)
        cprof = CafeProfileForm(request.POST, request.FILES)

        if form2.is_valid() and cprof.is_valid():
            user = form2.save()

            profile = cprof.save(commit=False)
            profile.user = user
            profile.save()

            username = form2.cleaned_data['username']
            password = form2.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    else:
        form2 = CafeSignUpForm()
        cprof = CafeProfileForm()
    context = {'form2': form2 , 'cprof': cprof}
    return render(request, 'authenticate/cafeRegister.html', context)




