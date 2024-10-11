from abc import ABC, abstractmethod

from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_custom_selection import SurveyCustomSelection


class SurveyCustomSelectionRepository(ABC):

    @abstractmethod
    def createSurveyCustomSelection(self, question: SurveyQuestion, custom_text: str) -> SurveyCustomSelection:
        pass

    @abstractmethod
    def findSurveyCustomSelectionListByQuestionId(self, question_id):
        pass