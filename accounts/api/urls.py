from rest_framework.routers import DefaultRouter
from .views import TutorialPhotoshopViewSet, TutorialIllustratorViewSet, CourseViewSet

tutorialphotoshop_router = DefaultRouter()
tutorialphotoshop_router.register(r'tutorialphotoshop', TutorialPhotoshopViewSet)

tutorialillustrator_router = DefaultRouter()
tutorialillustrator_router.register(r'tutorialillustrator', TutorialIllustratorViewSet)

course_router = DefaultRouter()
course_router.register(r'course', CourseViewSet)