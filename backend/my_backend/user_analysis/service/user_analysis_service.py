from abc import ABC, abstractmethod

class UserAnalysisService(ABC):
    @abstractmethod
    def createUserAnalysis(self, title, description):
        pass

    @abstractmethod
    def createUserAnalysisQuestion(self, user_analysis_id, question_text, user_analysis_type):
        pass

    @abstractmethod
    def createUserAnalysisCustomSelection(self, question_id, custom_text):
        pass

    @abstractmethod
    def saveAnswer(self, answers, account_Id):
        pass

    @abstractmethod
    def listAnswer(self, filter, user_analysis_id=None, question_id=None, account_id=None):
        pass

    @abstractmethod
    def listQuestions(self, user_analysis_id):
        pass

    @abstractmethod
    def listSelections(self, question_id):
        pass

    @abstractmethod
    def listUserAnalysis(self):
        pass