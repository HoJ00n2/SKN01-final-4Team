from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from user_analysis.entity.user_analysis_question import UserAnalysisQuestion
from user_analysis.repository.user_analysis_fixed_boolean_selection_repository_impl import \
    UserAnalysisFixedBooleanSelectionRepositoryImpl
from user_analysis.repository.user_analysis_fixed_five_score_selection_repository_impl import \
    UserAnalysisFixedFiveScoreSelectionRepositoryImpl
from user_analysis.repository.user_analysis_question_repository import UserAnalysisQuestionRepository


class UserAnalysisQuestionRepositoryImpl(UserAnalysisQuestionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__userAnalysisFixedFiveScoreSelectionRepository = UserAnalysisFixedFiveScoreSelectionRepositoryImpl.getInstance()
            cls.__instance.__userAnalysisFixedBooleanSelectionRepository = UserAnalysisFixedBooleanSelectionRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, user_analysis, question_text, user_analysis_type):
        try:
            question = UserAnalysisQuestion(user_analysis=user_analysis, question_text=question_text, user_analysis_type=user_analysis_type)
            if question.user_analysis_type == 2:
                self.__userAnalysisFixedFiveScoreSelectionRepository.create()
            elif question.user_analysis_type == 3:
                self.__userAnalysisFixedBooleanSelectionRepository.create()

            question.save()
            return question

        except IntegrityError as e:
            raise IntegrityError(f"Error creating survey question: {e}")

    def findUserAnalysisQuestionListByUserAnalysisId(self, user_analysis_id):
        return UserAnalysisQuestion.objects.filter(user_analysis_id=user_analysis_id)

    def findById(self, user_analysis_question_id):
        try:
            return UserAnalysisQuestion.objects.get(id=user_analysis_question_id)
        except ObjectDoesNotExist:
            return None