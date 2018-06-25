from django.conf.urls import url, include
from app.models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')
