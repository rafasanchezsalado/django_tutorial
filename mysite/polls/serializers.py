from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedRelatedField(
        many=False, view_name="question-detail", read_only=True
    )
    pub_date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Question
        fields = ["id", "question_text", "pub_date"]


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedRelatedField(
        many=False, view_name="choice-detail", read_only=True
    )

    class Meta:
        model = Choice
        fields = ["id", "question", "choice_text", "votes"]
