from django.db import models

from user_analysis.entity.user_analysis_question import UserAnalysisQuestion


class UserAnalysisQuestionImage(models.Model):
    id = models.AutoField(primary_key=True)
    user_analysis_question_id = models.ForeignKey(UserAnalysisQuestion, on_delete=models.CASCADE)
    question_image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'user_analysis_question_image'
        app_label = 'user_analysis'