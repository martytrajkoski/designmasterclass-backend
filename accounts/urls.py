from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile, name='home'),
    path('courses/', views.courses),
    path('subscription/', views.subscription),
]
