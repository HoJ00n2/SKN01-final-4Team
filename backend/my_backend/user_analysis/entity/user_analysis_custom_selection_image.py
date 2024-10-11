from django.db import models

from user_analysis.entity.user_analysis_custom_selection import UserAnalysisCustomSelection


class UserAnalysisCustomSelectionImage(models.Model):
    id = models.AutoField(primary_key=True)
    custom_selection_id = models.ForeignKey(UserAnalysisCustomSelection, on_delete=models.CASCADE)
    selection_image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'user_analysis_custom_selection_image'
        app_label = 'user_analysis'