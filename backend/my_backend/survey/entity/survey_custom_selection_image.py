from django.db import models

from survey.entity.survey_custom_selection import SurveyCustomSelection


class SurveyCustomSelectionImage(models.Model):
    id = models.AutoField(primary_key=True)
    custom_selection_id = models.ForeignKey(SurveyCustomSelection, on_delete=models.CASCADE)
    selection_image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'survey_custom_selection_image'
        app_label = 'survey'