from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from survey.entity.survey import Survey
from survey.entity.survey_question import SurveyQuestion
from survey.repository.survey_fixed_boolean_selection_repository_impl import SurveyFixedBooleanSelectionRepositoryImpl
from survey.repository.survey_fixed_five_score_selection_repository_impl import \
    SurveyFixedFiveScoreSelectionRepositoryImpl
from survey.repository.survey_question_repository import SurveyQuestionRepository


class SurveyQuestionRepositoryImpl(SurveyQuestionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
            cls.__instance.__surveyFixedFiveScoreSelectionRepository = SurveyFixedFiveScoreSelectionRepositoryImpl.getInstance()
            cls.__instance.__surveyFixedBooleanSelectionRepository = SurveyFixedBooleanSelectionRepositoryImpl.getInstance()

        return cls.__instance

    def create(self, survey, question_text, survey_type):
        # if not isinstance(survey, Survey):
        #     raise ValueError("Survey must be an instance of Survey")

        try:
            question = SurveyQuestion(survey=survey, question_text=question_text, survey_type=survey_type)
            if question.survey_type == 2:
                self.__surveyFixedFiveScoreSelectionRepository.create()
            elif question.survey_type == 3:
                self.__surveyFixedBooleanSelectionRepository.create()
            question.save()
            return question

        except IntegrityError as e:
            raise IntegrityError(f"Error creating survey question: {e}")


    def findSurveyQuestionListBySurveyId(self, survey_id):
        return SurveyQuestion.objects.filter(survey_id=survey_id)


    def findById(self, survey_question_id):
        try:
            return SurveyQuestion.objects.get(id=survey_question_id)
        except ObjectDoesNotExist:
            return None