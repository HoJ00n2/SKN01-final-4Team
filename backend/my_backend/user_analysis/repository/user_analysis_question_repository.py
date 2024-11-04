from abc import ABC, abstractmethod

class UserAnalysisQuestionRepository(ABC):
    @abstractmethod
    def create(self, user_analysis, question_text, user_analysis_type):
        pass

    @abstractmethod
    def findUserAnalysisQuestionListByUserAnalysisId(self, user_analysis_id):
        pass

    @abstractmethod
    def findById(self, user_analysis_question_id):
        pass
