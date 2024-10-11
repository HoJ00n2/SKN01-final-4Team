from django.db import models

from survey.entity.survey import Survey
from survey.entity.survey_type import SurveyType


class SurveyQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    # survey_id = survey 객체를 의미
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    survey_type = models.IntegerField(
        choices=SurveyType.choices,
        default=SurveyType.GENERAL
    )

    def __str__(self):
        return f"question_text: {self.question_text}, survey_type: {self.get_survey_type_display()}, survey_id: {self.survey.id}"

    class Meta:
        db_table = 'survey_question'
        app_label = 'survey'