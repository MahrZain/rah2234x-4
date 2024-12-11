from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')