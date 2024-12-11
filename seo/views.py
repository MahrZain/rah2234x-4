from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'login.html')
    

def login_request(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please enter both username and password.')
            return render(request, 'login.html') 

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.error(request, "Login Failed! Check Your Credentials!")
            return render(request, 'login.html') 


    return render(request, 'login.html')
