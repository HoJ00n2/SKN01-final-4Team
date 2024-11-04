from abc import ABC, abstractmethod
class BoardRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    # add
    @abstractmethod
    def create(self, boardData):
        pass