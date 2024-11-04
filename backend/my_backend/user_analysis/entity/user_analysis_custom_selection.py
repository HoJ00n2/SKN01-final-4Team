from django.db import models

from user_analysis.entity.user_analysis_question import UserAnalysisQuestion


class UserAnalysisCustomSelection(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(UserAnalysisQuestion, related_name='selections', on_delete=models.CASCADE)
    custom_text = models.CharField(max_length=255)

    def __str__(self):
        return self.custom_text

    class Meta:
        db_table = 'user_analysis_custom_selection'
        app_label = 'user_analysis'