from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from .validations import custom_validation, validate_email, validate_password
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from ..models import TutorialPhotoshop, TutorialIllustrator, Course, Quiz
from .serializers import TutorialPhotoshopSerializer, TutorialIllustratorSerializer, CourseSerializer, UserRegisterSerializer, UserLoginSerializer, UserViewSerializer, QuizSerializer 
import stripe
from django.conf import settings

class TutorialPhotoshopViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = TutorialPhotoshop.objects.all()
    serializer_class = TutorialPhotoshopSerializer

class TutorialIllustratorViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = TutorialIllustrator.objects.all()
    serializer_class = TutorialIllustratorSerializer

UserModel = get_user_model()
class UserRegisterViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
class UserLoginViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def create(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(serializer.data)
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

class UserLogoutViewSet(ViewSet):    
	permission_classes = (permissions.AllowAny,)

	def create(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)

class UserViewViewSet(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        serializer = UserViewSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
    def create(self, request):
        print(request.data) 
        serializer = UserViewSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UserCourseAddViewSet(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request):
        user = request.user
        course_id = request.data.get('course')
        print(user)
        print(course_id)
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.courses.add(course)
        user.save()

        serializer = UserViewSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
class UserCourseRemoveViewSet(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request):
        user = request.user
        course_id = request.data.get('course')

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.courses.remove(course)
        user.save()

        serializer = UserViewSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
class UserCourseListViewSet(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        user = request.user

        try:
            courses = user.courses.all()
            serializer = CourseSerializer(courses, many=True)
            return Response({'courses': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserQuizAddViewSet(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request):
        user = request.user
        quiz_id = request.data.get('quiz')
        print(user)
        print(quiz_id)
        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.quizzes.add(quiz)
        user.save()

        serializer = UserViewSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
class UserQuizRemoveViewSet(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request):
        user = request.user
        quiz_id = request.data.get('quiz')

        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.quizzes.remove(quiz)
        user.save()

        serializer = UserViewSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
class UserQuizListViewSet(ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        user = request.user

        try:
            quizzes = user.quizzes.all()
            serializer = QuizSerializer(quizzes, many=True)
            return Response({'quizzes': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCheckoutViewSet(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': course.stripe_price_id,
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment',
                success_url=settings.SITE_URL + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '?canceled=true',
            )
            return Response(checkout_session.url)
        except Exception as e:
            return Response(
                {'error': f'Something went wrong when creating stripe checkout session: {e}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR 
            )