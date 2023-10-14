from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TutorialViewSet

tutorial_router = DefaultRouter()
tutorial_router.register(r'tutorials', TutorialViewSet)