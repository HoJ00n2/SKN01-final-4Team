from django.core.paginator import Paginator
from django.db import IntegrityError

from user_analysis.entity.user_analysis import UserAnalysis
from user_analysis.repository.user_analysis_repository import UserAnalysisRepository


class UserAnalysisRepositoryImpl(UserAnalysisRepository):
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

    def create(self, title, description):
        user_analysis = UserAnalysis(title=title, description=description)
        user_analysis.save()

        return user_analysis

    def findById(self, user_analysis_id):
        try:
            return UserAnalysis.objects.get(id=user_analysis_id)
        except UserAnalysis.DoesNotExist:
            return None

    def list(self):
        return UserAnalysis.objects.all()
