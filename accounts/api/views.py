from rest_framework.viewsets import ModelViewSet
from ..models import TutorialPhotoshop, TutorialIllustrator, Course
from .serializers import TutorialPhotoshopSerializer, TutorialIllustratorSerializer, CourseSerializer

class TutorialPhotoshopViewSet(ModelViewSet):
    queryset = TutorialPhotoshop.objects.all()
    serializer_class = TutorialPhotoshopSerializer

class TutorialIllustratorViewSet(ModelViewSet):
    queryset = TutorialIllustrator.objects.all()
    serializer_class = TutorialIllustratorSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer