from rest_framework.viewsets import ModelViewSet
from ..models import Tutorial
from .serializers import TutorialSerializer

class TutorialViewSet(ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer