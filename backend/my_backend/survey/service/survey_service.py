from abc import ABC, abstractmethod

class SurveyService(ABC):
    @abstractmethod
    def createSurvey(self, title, description):
        pass

    @abstractmethod
    def createSurveyQuestion(self, survey_id, question_text, survey_type):
        pass

    @abstractmethod
    def createSurveyCustomSelection(self, question_id, custom_text):
        pass

    @abstractmethod
    def saveAnswer(self, answers, account_Id):
        pass

    @abstractmethod
    def listAnswer(self, filter, survey_id=None, question_id=None, account_id=None):
        pass

    @abstractmethod
    def listQuestions(self, survey_id):
        pass

    @abstractmethod
    def listSelections(self, question_id):
        pass

    @abstractmethod
    def listSurvey(self):
        pass
