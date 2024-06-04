from abc import ABC, abstractmethod

from MicroRTS_NB import GameState

from ai.ai import AI

class SelfPlay(ABC):
    @abstractmethod
    def update(self, prog)->None:
        pass
    
    @abstractmethod
    def getN(self)->int:
        pass
    
    @abstractmethod
    def evaluate(self,  a1 : AI, gs : GameState, max_tick :int)->float:
        pass
    
    @abstractmethod
    def getBest(self)->AI:
        pass
    
    @abstractmethod
    def getIndividual(self)->AI:
        pass
    
    @abstractmethod
    def stoppingCriterion(score)->bool:
        pass