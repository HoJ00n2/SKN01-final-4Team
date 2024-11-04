from django.db import models
from account.entity.account import Account
from survey.entity.survey import Survey
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_fixed_five_score_selection import SurveyFixedFiveScoreSelection
from survey.entity.survey_fixed_boolean_selection import SurveyFixedBooleanSelection
from survey.entity.survey_custom_selection import SurveyCustomSelection


class SurveyAnswer(models.Model):
    survey = models.ForeignKey(Survey, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True) # 서술형 답변
    five_score_selection = models.ForeignKey(SurveyFixedFiveScoreSelection, blank=True, null=True, on_delete=models.SET_NULL)
    boolean_selection = models.ForeignKey(SurveyFixedBooleanSelection, blank=True, null=True, on_delete=models.SET_NULL)
    custom_selection = models.ForeignKey(SurveyCustomSelection, blank=True, null=True, on_delete=models.SET_NULL)
    account = models.ForeignKey(Account, related_name='survey_answers', on_delete=models.CASCADE, null=True, default=None)

    response_order = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.account and self.survey and self.question and self.response_order is None:
            last_order = SurveyAnswer.objects.filter(
                account=self.account,
                survey=self.survey,
                question=self.question
            ).aggregate(models.Max('response_order'))['response_order__max']

            self.response_order = (last_order or 0) + 1

        super(SurveyAnswer, self).save(*args, **kwargs)

    def __str__(self):
        return f"Answer to {self.question.question_text}"

    class Meta:
        db_table = 'survey_answer'
        app_label = 'survey'