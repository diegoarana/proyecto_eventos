from app.models import Choice
from rest_framework import routers, serializers, viewsets

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')
