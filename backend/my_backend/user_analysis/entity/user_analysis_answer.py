from django.db import models
from account.entity.account import Account
from user_analysis.entity.user_analysis_custom_selection import UserAnalysisCustomSelection
from user_analysis.entity.user_analysis_fixed_boolean_selection import UserAnalysisFixedBooleanSelection
from user_analysis.entity.user_analysis_fixed_five_score_selection import UserAnalysisFixedFiveScoreSelection

from user_analysis.entity.user_analysis import UserAnalysis
from user_analysis.entity.user_analysis_question import UserAnalysisQuestion


class UserAnalysisAnswer(models.Model):
    user_analysis = models.ForeignKey(UserAnalysis, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(UserAnalysisQuestion, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    five_score_selection = models.ForeignKey(UserAnalysisFixedFiveScoreSelection, blank=True, null=True, on_delete=models.SET_NULL)
    boolean_selection = models.ForeignKey(UserAnalysisFixedBooleanSelection, blank=True, null=True, on_delete=models.SET_NULL)
    custom_selection = models.ForeignKey(UserAnalysisCustomSelection, blank=True, null=True, on_delete=models.SET_NULL)
    account = models.ForeignKey(Account, related_name='user_analysis_answers', on_delete=models.CASCADE, null=True, default=None)

    response_order = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.account and self.user_analysis and self.question and self.response_order is None:
            last_order = UserAnalysisAnswer.objects.filter(
                account=self.account,
                user_analysis=self.user_analysis,
                question=self.question
            ).aggregate(models.Max('response_order'))['response_order__max']

            self.response_order = (last_order or 0) + 1

        super(UserAnalysisAnswer, self).save(*args, **kwargs)

    def __str__(self):
        return f"Answer to {self.question.question_text}"

    class Meta:
        db_table = 'user_analysis_answer'
        app_label = 'user_analysis'