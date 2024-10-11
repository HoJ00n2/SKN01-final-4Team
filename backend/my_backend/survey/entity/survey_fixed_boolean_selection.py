from django.db import models
from survey.entity.survey_question import SurveyQuestion

class SurveyFixedBooleanSelection(models.Model):
    id = models.AutoField(primary_key=True)
    is_true = models.BooleanField()

    def __str__(self):
        return str(self.is_true)

    class Meta:
        db_table = 'survey_fixed_boolean_selection'
        app_label = 'survey'
