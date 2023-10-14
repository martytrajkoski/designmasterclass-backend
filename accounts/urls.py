from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile),
    path('courses/', views.courses),
    path('subscription/', views.subscription),
]
