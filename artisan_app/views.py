import django
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.


def home(request):
    return render(request, '../templates/home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            error_message = "Passwords do not match."
            return render(request, '../templates/register.html', {'error_message': error_message})

        user = User.objects.create_user(username = first_name + " " + last_name, email = email, 
                                        password = password)

        return redirect('home')


    return render(request, '../templates/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid email or password."
            return render(request, '../templates/login.html', {'error_message': error_message})

    return render(request, '../templates/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')