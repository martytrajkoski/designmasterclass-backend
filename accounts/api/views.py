from rest_framework.viewsets import ModelViewSet
from ..models import TutorialPhotoshop, TutorialIllustrator
from .serializers import TutorialPhotoshopSerializer, TutorialIllustratorSerializer

class TutorialPhotoshopViewSet(ModelViewSet):
    queryset = TutorialPhotoshop.objects.all()
    serializer_class = TutorialPhotoshopSerializer

class TutorialIllustratorViewSet(ModelViewSet):
    queryset = TutorialIllustrator.objects.all()
    serializer_class = TutorialIllustratorSerializer