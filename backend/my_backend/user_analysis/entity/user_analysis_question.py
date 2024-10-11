from django.db import models

from user_analysis.entity.user_analysis import UserAnalysis
from user_analysis.entity.user_analysis_type import UserAnalysisType


class UserAnalysisQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    user_analysis = models.ForeignKey(UserAnalysis, related_name='user_analysis_questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    user_analysis_type = models.IntegerField(
        choices=UserAnalysisType.choices,
        default=UserAnalysisType.GENERAL
    )

    def __str__(self):
        return f"question_text: {self.question_text}, user_analysis_type: {self.user_analysis_type}, user_analysis_id: {self.user_analysis.id}"

    class Meta:
        db_table = 'user_analysis_question'
        app_label = 'user_analysis'