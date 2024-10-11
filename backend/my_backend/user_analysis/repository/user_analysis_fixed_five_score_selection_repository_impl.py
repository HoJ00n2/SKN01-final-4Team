from user_analysis.entity.user_analysis_fixed_five_score_selection import UserAnalysisFixedFiveScoreSelection
from user_analysis.repository.user_analysis_fixed_five_score_selection_repository import \
    UserAnalysisFixedFiveScoreSelectionRepository


class UserAnalysisFixedFiveScoreSelectionRepositoryImpl(UserAnalysisFixedFiveScoreSelectionRepository):
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
            if not UserAnalysisFixedFiveScoreSelection.objects.filter(score=score).exists():
                UserAnalysisFixedFiveScoreSelection.objects.create(score=score)