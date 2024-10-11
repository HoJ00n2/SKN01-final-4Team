from django.db import IntegrityError

from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_custom_selection import SurveyCustomSelection
from survey.repository.survey_custom_selection_repository import SurveyCustomSelectionRepository


class SurveyCustomSelectionRepositoryImpl(SurveyCustomSelectionRepository):
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

    def createSurveyCustomSelection(self, question, custom_text):
        if not isinstance(question, SurveyQuestion):
            raise ValueError("Question must be an instance of SurveyQuestion")

        try:
            selection = SurveyCustomSelection(question=question, custom_text=custom_text)
            selection.save()
            return selection

        except IntegrityError as e:
            raise IntegrityError(f"Error creating survey selection: {e}")

    def findSurveyCustomSelectionListByQuestionId(self, question_id):
        return SurveyCustomSelection.objects.filter(question_id=question_id)



