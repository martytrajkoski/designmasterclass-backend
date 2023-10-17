from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TutorialPhotoshopViewSet, TutorialIllustratorViewSet

tutorialphotoshop_router = DefaultRouter()
tutorialphotoshop_router.register(r'tutorialphotoshop', TutorialPhotoshopViewSet)

tutorialillustrator_router = DefaultRouter()
tutorialillustrator_router.register(r'tutorialillustrator', TutorialIllustratorViewSet)