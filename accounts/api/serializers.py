from rest_framework.serializers import ModelSerializer
from ..models import Tutorial

class TutorialSerializer(ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'name', 'category', 'content1', 'content2', 'content3', 'content4',
                  'content5', 'image1', 'image2', 'image3', 'image4', 'image5')