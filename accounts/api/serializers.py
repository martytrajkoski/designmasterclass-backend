from rest_framework.serializers import ModelSerializer
from ..models import TutorialPhotoshop, TutorialIllustrator, Course

class TutorialPhotoshopSerializer(ModelSerializer):
    class Meta:
        model = TutorialPhotoshop
        fields = ('id', 'name', 'content1', 'content2', 'content3', 'content4',
                  'content5', 'image1', 'image2', 'image3', 'image4', 'image5')
        
class TutorialIllustratorSerializer(ModelSerializer):
    class Meta:
        model = TutorialIllustrator
        fields = ('id', 'name', 'content1', 'content2', 'content3', 'content4',
                  'content5', 'image1', 'image2', 'image3', 'image4', 'image5')
        
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'price', 'content', 'description', 'length',
                  'dateCreated', 'link', 'thumbnail')