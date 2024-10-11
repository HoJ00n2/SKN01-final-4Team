from abc import ABC, abstractmethod

class SurveyFixedBooleanSelectionRepository(ABC):

    @abstractmethod
    def create(self):
        pass