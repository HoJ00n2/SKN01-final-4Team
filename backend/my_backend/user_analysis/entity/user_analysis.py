from django.db import models


class UserAnalysis(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)


    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'user_analysis'
        app_label = 'user_analysis'