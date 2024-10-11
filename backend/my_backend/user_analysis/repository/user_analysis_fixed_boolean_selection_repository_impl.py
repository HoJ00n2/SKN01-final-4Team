from user_analysis.entity.user_analysis_fixed_boolean_selection import UserAnalysisFixedBooleanSelection
from user_analysis.repository.user_analysis_fixed_boolean_selection_repository import \
    UserAnalysisFixedBooleanSelectionRepository


class UserAnalysisFixedBooleanSelectionRepositoryImpl(UserAnalysisFixedBooleanSelectionRepository):
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
        if not UserAnalysisFixedBooleanSelection.objects.filter(is_true=True).exists():
            UserAnalysisFixedBooleanSelection.objects.create(is_true=True)
        if not UserAnalysisFixedBooleanSelection.objects.filter(is_true=False).exists():
            UserAnalysisFixedBooleanSelection.objects.create(is_true=False)