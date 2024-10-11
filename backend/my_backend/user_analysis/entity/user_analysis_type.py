from django.db import models
from django.utils.translation import gettext_lazy as _

class UserAnalysisType(models.TextChoices):
    GENERAL = '1', 'General'
    FIVE_SCORE = '2', 'Five Score'
    BOOLEAN = '3', 'Boolean'
    CUSTOM = '4', 'Custom'
