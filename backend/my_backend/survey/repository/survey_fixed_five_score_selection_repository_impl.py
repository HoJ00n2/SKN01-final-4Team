from survey.entity.survey_fixed_five_score_selection import SurveyFixedFiveScoreSelection
from survey.repository.survey_fixed_five_score_selection_repository import SurveyFixedFiveScoreSelectionRepository


class SurveyFixedFiveScoreSelectionRepositoryImpl(SurveyFixedFiveScoreSelectionRepository):
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
        for score in range(1, 6):
            if not SurveyFixedFiveScoreSelection.objects.filter(score=score).exists():
                SurveyFixedFiveScoreSelection.objects.create(score=score)