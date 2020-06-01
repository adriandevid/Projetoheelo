from abc import ABC, abstractmethod

class IWindowQuizRepository(ABC):
    @abstractmethod
    def Add(self):
        pass
    @abstractmethod
    def Remove(self):
        pass
    @abstractmethod
    def Update(self):
        pass
    @abstractmethod
    def RegisterQuiz(self):
        pass