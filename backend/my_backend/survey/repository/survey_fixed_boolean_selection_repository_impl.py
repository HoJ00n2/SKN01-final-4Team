from django.db import migrations

from survey.entity.survey_fixed_boolean_selection import SurveyFixedBooleanSelection
from survey.repository.survey_fixed_boolean_selection_repository import SurveyFixedBooleanSelectionRepository


class SurveyFixedBooleanSelectionRepositoryImpl(SurveyFixedBooleanSelectionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    def create(self):
        if not SurveyFixedBooleanSelection.objects.filter(is_true=True).exists():
            SurveyFixedBooleanSelection.objects.create(is_true=True)
        if not SurveyFixedBooleanSelection.objects.filter(is_true=False).exists():
            SurveyFixedBooleanSelection.objects.create(is_true=False)
