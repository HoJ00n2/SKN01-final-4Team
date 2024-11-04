from django.db import models

class UserAnalysisFixedBooleanSelection(models.Model):
    id = models.AutoField(primary_key=True)
    is_true = models.BooleanField()

    def __str__(self):
        return str(self.is_true)

    class Meta:
        db_table = 'user_analysis_fixed_boolean_selection'
        app_label = 'user_analysis'
