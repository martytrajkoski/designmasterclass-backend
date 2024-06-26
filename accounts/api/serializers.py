from django.forms import ValidationError
from rest_framework import serializers
from ..models import TutorialPhotoshop, TutorialIllustrator, Course, Quiz
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(allow_empty=False, many=True, queryset=Course.objects.all(), required=False)
    quizzes = serializers.PrimaryKeyRelatedField(allow_empty=False, many=True, queryset=Quiz.objects.all(), required=False)
    class Meta:
        model = UserModel
        fields='__all__'

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(email=clean_data['email'],
                                                 password=clean_data['password'])
        user_obj.username = clean_data['username']
        user_obj.firstName = clean_data['firstName']
        user_obj.lastName = clean_data['lastName']
        user_obj.save()
        return user_obj

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = UserModel
        fields = ['email', 'password'] 

    def check_user(self, clean_data):
        print("Email:", clean_data['email'])
        print("Password:", clean_data['password'])
        user = authenticate(email=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('User not found')
        return user
    
class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'username', 'firstName', 'lastName', 'courses', 'quizzes')

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'artist', 'category', 'length', 'url', 'thumbnail', 'dateCreated')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'artist', 'price', 'rating', 'category', 'length', 'dateCreated', 'url', 'thumbnail', 'stripe_price_id')
        
class TutorialPhotoshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialPhotoshop
        fields = ('id', 'name', 'content1', 'content2', 'content3', 'content4',
                  'content5', 'image1', 'image2', 'image3', 'image4', 'image5')
        
class TutorialIllustratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialIllustrator
        fields = ('id', 'name', 'content1', 'content2', 'content3', 'content4',
                  'content5', 'image1', 'image2', 'image3', 'image4', 'image5')