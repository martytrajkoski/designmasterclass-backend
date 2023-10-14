from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request):
    return render(request, 'accounts/profile.html')

def courses(request):
    return render(request, 'accounts/courses.html')

def subscription(request):
    return render(request, 'accounts/subscription.html')