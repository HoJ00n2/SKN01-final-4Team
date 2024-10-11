from abc import ABC, abstractmethod


class UserAnalysisRepository(ABC):
    @abstractmethod
    def create(self, title, description):
        pass

    @abstractmethod
    def findById(self, user_analysis_id):
        pass

    @abstractmethod
    def list(self):
        pass
