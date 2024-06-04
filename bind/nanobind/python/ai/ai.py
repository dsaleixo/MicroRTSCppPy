from abc import ABC, abstractmethod

from MicroRTS_NB import GameState

class AI(ABC):
    @abstractmethod
    def getActions(self, gs : GameState,player : int):
        pass
    
    @abstractmethod
    def resert(self):
        pass
    
    