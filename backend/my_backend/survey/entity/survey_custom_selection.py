from django.db import models

from survey.entity.survey_question import SurveyQuestion


class SurveyCustomSelection(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(SurveyQuestion, related_name='selections', on_delete=models.CASCADE)
    custom_text = models.CharField(max_length=255)

    def __str__(self):
        return self.custom_text

    class Meta:
        db_table = 'survey_custom_selection'
        app_label = 'survey'