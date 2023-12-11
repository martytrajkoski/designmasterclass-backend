from django.shortcuts import render
from django.http import HttpResponse
from .models import TutorialIllustrator

# Create your views here.

def profile(request):
    illustrator = TutorialIllustrator.objects.all()
    context = {
        'illustrator': illustrator
    }
    return render(request, 'accounts/profile.html', context)

def courses(request):
    return render(request, 'accounts/courses.html')

def subscription(request):
    return render(request, 'accounts/subscription.html')