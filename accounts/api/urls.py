from rest_framework.routers import DefaultRouter
from .views import TutorialPhotoshopViewSet, TutorialIllustratorViewSet, CourseViewSet, QuizViewSet, UserLoginViewSet, UserLogoutViewSet, UserRegisterViewSet, UserViewViewSet
from django.urls import path, include

# urlpatterns = [
# 	path('login/', UserLoginViewSet.as_view(), name='login'),
#     path('logout/', UserLogoutViewSet.as_view(), name='logout'),
#     path('register/', UserRegisterViewSet.as_view(), name='register'),
#     path('user/', UserViewViewSet.as_view(), name='user'),
# ]
router = DefaultRouter()
router.register(r'tutorialphotoshop', TutorialPhotoshopViewSet)
router.register(r'tutorialillustrator', TutorialIllustratorViewSet)

router.register(r'userlogin', UserLoginViewSet, basename='userlogin')
router.register(r'userlogout', UserLogoutViewSet, basename='userlogout')
router.register(r'userregister', UserRegisterViewSet, basename='userregister')
router.register(r'userview', UserViewViewSet, basename='userview')

router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
]

# {
#     "email": "test@example.com",
#     "username": "tester",
#     "password": "tester123"
# }