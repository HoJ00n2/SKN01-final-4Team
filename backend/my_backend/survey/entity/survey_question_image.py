from django.db import models

from survey.entity.survey_question import SurveyQuestion


class SurveyQuestionImage(models.Model):
    id = models.AutoField(primary_key=True)
    survey_question_id = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    question_image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'survey_question_image'
        app_label = 'survey'