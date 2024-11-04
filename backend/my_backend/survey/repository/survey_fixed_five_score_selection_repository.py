from abc import ABC, abstractmethod

class SurveyFixedFiveScoreSelectionRepository(ABC):

    @abstractmethod
    def create(self):
        pass