from account.entity.account import Account
from survey.entity.survey_fixed_boolean_selection import SurveyFixedBooleanSelection
from survey.entity.survey_fixed_five_score_selection import SurveyFixedFiveScoreSelection
from survey.entity.survey import Survey
from survey.entity.survey_answer import SurveyAnswer
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_custom_selection import SurveyCustomSelection
from survey.repository.survey_question_repository_impl import SurveyQuestionRepositoryImpl
from survey.repository.survey_answer_repository import SurveyAnswerRepository
from django.db import IntegrityError

from survey.repository.survey_repository_impl import SurveyRepositoryImpl


class SurveyAnswerRepositoryImpl(SurveyAnswerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__surveyQuestionRepository = SurveyQuestionRepositoryImpl.getInstance()
            cls.__instance.__surveyRepository = SurveyRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def saveAnswer(self, survey_id, question_id, answer_data, account_id):
        # if not isinstance(question_id, SurveyQuestion):
        #     raise ValueError("Question must be an instance of SurveyQuestion")
        try:
            question = self.__surveyQuestionRepository.findById(question_id)

            survey = Survey.objects.get(id = survey_id)
            if account_id == True:
                account = Account.objects.get(id=account_id)
            else:
                account = account_id

            if question.survey_type == 1: # General
                answer = SurveyAnswer(
                    survey=survey,
                    question=question,
                    answer_text=answer_data,
                    account=account
                )
      
            elif question.survey_type == 2: # Five Score
                five_score_selection = SurveyFixedFiveScoreSelection.objects.get(score=answer_data)
                answer = SurveyAnswer(
                    survey=survey,
                    question=question,
                    five_score_selection=five_score_selection,
                    account=account
                )
        
            elif question.survey_type == 3: # Boolean
                boolean_selection = SurveyFixedBooleanSelection.objects.get(is_true=answer_data)
                answer = SurveyAnswer(
                    survey=survey,
                    question=question,
                    boolean_selection=boolean_selection,
                    account=account
                )
                
            elif question.survey_type == 4:  # Custom
                custom_selection = SurveyCustomSelection.objects.get(custom_text=answer_data)
                answer = SurveyAnswer(
                    survey=survey,
                    question=question,
                    custom_selection=custom_selection,
                    account=account
                )


            answer.save()
            return answer

        except IntegrityError as e:
            raise IntegrityError(f"Error saving survey answer: {e}")

    def summarizeAnswerBySurveyId(self, survey_id):
        summerizedAnswer = SurveyAnswer.objects.filter(survey_id=survey_id)
        return summerizedAnswer

    def summerizeAnswerByQuestionId(self, question_id):
        summerizedAnswer = SurveyAnswer.objects.filter(question_id=question_id)
        return summerizedAnswer

    def summerizeAnswerByAccountId(self, account_id):
        summerizedAnswer = SurveyAnswer.objects.filter(account_id=account_id)
        return summerizedAnswer

    def summerizeAnswerBySurveyIdandAccountId(self, survey_id, account_id):
        summerizedAnswer = SurveyAnswer.objects.filter(survey_id=survey_id, account_id=account_id)
        return summerizedAnswer
