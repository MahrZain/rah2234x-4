# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from throttle.decorators import throttle
from data.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.utils import timezone

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        action_type = request.POST.get('actiontype')

        # Validate input
        if not ip or not action_type:
            messages.error(request, 'Please enter both IP address and action type.')
            return render(request, 'home.html')

        # Check if the IP already exists
        existing_entry = CustomUser.objects.filter(IP=ip).first()
        if existing_entry:
            messages.error(request, f"IP address '{ip}' already exists with action type '{existing_entry.type}'.")
            return render(request, 'home.html')

        # Save the new entry
        try:
            custom_user = CustomUser(user=request.user, IP=ip, type=action_type)
            custom_user.save()
            # Count how many submissions the user has made today
            today = timezone.now().date()
            daily_count = CustomUser.objects.filter(user=request.user, created_at__date=today).count()
            messages.success(request, f"Submission Successful! You have made {daily_count} submissions today.")
        except Exception as e:
            messages.error(request, f"An error occurred while saving: {e}")
        
        return render(request, 'home.html',{'data': daily_count})
    
    # If GET request, just show the home page
    return render(request, 'home.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'login.html')

@throttle(zone='default')
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
            messages.error(request, "Login Failed! Check your credentials.")
            return render(request, 'login.html') 

    return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        request.session.flush()
        messages.success(request, "Logout Successful!")
        return redirect('login-user')
    else:
        return render(request, 'login.html')
