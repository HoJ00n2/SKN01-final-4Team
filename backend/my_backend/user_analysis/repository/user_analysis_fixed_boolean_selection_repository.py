from abc import ABC, abstractmethod

class UserAnalysisFixedBooleanSelectionRepository(ABC):

    @abstractmethod
    def create(self):
        pass