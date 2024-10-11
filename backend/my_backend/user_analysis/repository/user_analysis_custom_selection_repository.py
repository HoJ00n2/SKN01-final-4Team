from abc import ABC, abstractmethod

from user_analysis.entity.user_analysis_custom_selection import UserAnalysisCustomSelection
from user_analysis.entity.user_analysis_question import UserAnalysisQuestion


class UserAnalysisCustomSelectionRepository(ABC):

    @abstractmethod
    def createUserAnalysisCustomSelection(self, question: UserAnalysisQuestion, custom_text: str) -> UserAnalysisCustomSelection:
        pass

    @abstractmethod
    def findUserAnalysisCustomSelectionListByQuestionId(self, question_id):
        pass