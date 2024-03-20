from rest_framework.routers import DefaultRouter
from .views import TutorialPhotoshopViewSet, TutorialIllustratorViewSet, CourseViewSet, QuizViewSet, UserCourseListViewSet, UserLoginViewSet, UserLogoutViewSet, UserQuizAddViewSet, UserQuizListViewSet, UserQuizRemoveViewSet, UserRegisterViewSet, UserViewViewSet, UserCourseAddViewSet, UserCourseRemoveViewSet, StripeCheckoutViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'tutorialphotoshop', TutorialPhotoshopViewSet)
router.register(r'tutorialillustrator', TutorialIllustratorViewSet)

router.register(r'userlogin', UserLoginViewSet, basename='userlogin')
router.register(r'userlogout', UserLogoutViewSet, basename='userlogout')
router.register(r'userregister', UserRegisterViewSet, basename='userregister')
router.register(r'userview', UserViewViewSet, basename='userview')

router.register(r'courses', CourseViewSet, basename='course')
router.register(r'add_course', UserCourseAddViewSet, basename='user-add-course')
router.register(r'remove_course', UserCourseRemoveViewSet, basename='user-remove-course')
router.register(r'list_course', UserCourseListViewSet, basename='user-list-course')

router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'add_quiz', UserQuizAddViewSet, basename='user-add-quiz')
router.register(r'remove_quiz', UserQuizRemoveViewSet, basename='user-remove-quiz')
router.register(r'list_quiz', UserQuizListViewSet, basename='user-list-quiz')

urlpatterns = [
    path('', include(router.urls)),
    path('create_checkout_session', StripeCheckoutViewSet.as_view())
]

# {
#     "email": "test@example.com",
#     "username": "tester",
#     "password": "tester123"
# }