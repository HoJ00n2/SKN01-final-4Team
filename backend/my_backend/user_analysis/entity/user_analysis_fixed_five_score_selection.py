from django.db import models

class UserAnalysisFixedFiveScoreSelection(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return str(self.score)

    class Meta:
        db_table = 'user_analysis_fixed_five_score_selection'
        app_label = 'user_analysis'