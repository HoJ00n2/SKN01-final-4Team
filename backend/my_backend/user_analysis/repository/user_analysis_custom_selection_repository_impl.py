from django.db import IntegrityError

from user_analysis.entity.user_analysis_custom_selection import UserAnalysisCustomSelection
from user_analysis.entity.user_analysis_question import UserAnalysisQuestion
from user_analysis.repository.user_analysis_custom_selection_repository import UserAnalysisCustomSelectionRepository


class UserAnalysisCustomSelectionRepositoryImpl(UserAnalysisCustomSelectionRepository):
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

    def createUserAnalysisCustomSelection(self, question, custom_text):
        if not isinstance(question, UserAnalysisQuestion):
            raise ValueError("Question must be an instance of SurveyQuestion")

        try:
            selection = UserAnalysisCustomSelection(question=question, custom_text=custom_text)
            selection.save()
            return selection

        except IntegrityError as e:
            raise IntegrityError(f"Error creating survey selection: {e}")

    def findUserAnalysisCustomSelectionListByQuestionId(self, question_id):
        return UserAnalysisCustomSelection.objects.filter(question_id=question_id)