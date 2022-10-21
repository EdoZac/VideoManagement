from .models import Question, Movie, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url', 'question_text', 'pub_date', 'movie']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['url', 'title', 'pub_date', 'author', 'genre']


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ['url', 'question', 'choice_text', 'votes']