from abc import ABC, abstractmethod

class SurveyAnswerRepository(ABC):

    @abstractmethod
    def saveAnswer(self, survey_id, question_id, answer_data, account_id):
        pass

    @abstractmethod
    def summarizeAnswerBySurveyId(self, survey_id):
        pass

    @abstractmethod
    def summerizeAnswerByQuestionId(self, question_id):
        pass

    @abstractmethod
    def summerizeAnswerByAccountId(self, account_id):
        pass

    @abstractmethod
    def summerizeAnswerBySurveyIdandAccountId(self, survey_id, account_id):
        pass

