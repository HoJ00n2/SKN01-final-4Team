from rest_framework import serializers

from account.serilaizers import ProfileSerializer
from survey.entity.survey_custom_selection import SurveyCustomSelection
from survey.entity.survey_fixed_boolean_selection import SurveyFixedBooleanSelection
from survey.entity.survey_fixed_five_score_selection import SurveyFixedFiveScoreSelection
from survey.entity.survey import Survey
from survey.entity.survey_answer import SurveyAnswer
from survey.entity.survey_question import SurveyQuestion


class SurveyAnswerSerializer(serializers.ModelSerializer):
    survey_title = serializers.CharField(source='survey.title', read_only=True)
    profile_nickname = serializers.CharField(source='account.profile.nickname', read_only=True)
    question_text = serializers.CharField(source='question.question_text', read_only=True)
    survey_custom_selection_text = serializers.CharField(source='survey_custom_selection.custom_text', read_only=True,
                                                  default=None)

    class Meta:
        model = SurveyAnswer
        fields = ('id', 'survey_title', 'profile_nickname', 'question_text', 'survey_custom_selection_text', 'answer_text',
                  'boolean_selection', 'five_score_selection', 'response_order', 'created_at')

    def to_representation(self, instance):
        # 기본 직렬화 데이터
        data = super(SurveyAnswerSerializer, self).to_representation(instance)

        # None 값을 가진 필드를 제외
        return {k: v for k, v in data.items() if v is not None}

class SurveyQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestion
        fields = ('id', 'question_text', 'survey_type')

class SurveyFixedFiveScoreSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyFixedFiveScoreSelection
        fields = ['id', 'score']

class SurveyFixedBooleanSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyFixedBooleanSelection
        fields = ['id', 'is_true']

class SurveyCustomSelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyCustomSelection
        fields = ('id', 'custom_text', 'question_id')

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'title', 'description']
