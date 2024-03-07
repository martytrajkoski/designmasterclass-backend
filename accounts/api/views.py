from rest_framework import permissions, status, viewsets
from .validations import custom_validation, validate_email, validate_password
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from ..models import TutorialPhotoshop, TutorialIllustrator, Course, Quiz
from .serializers import TutorialPhotoshopSerializer, TutorialIllustratorSerializer, CourseSerializer, UserRegisterSerializer, UserLoginSerializer, UserViewSerializer, QuizSerializer 

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
    
class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer