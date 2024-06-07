
from abc import ABC, abstractmethod

from selfPlay.selfPlay import SelfPlay



class Individual(ABC):
    @abstractmethod
    def indToProg(self, ind):
        pass
    
    @abstractmethod
    def getNeighborhood(self, ind, n_neighborhood):
        pass
    
    @abstractmethod
    def progToInd(self,prog):
        pass
    
    @abstractmethod
    def toString(self,ind):
        pass
    
   
    
    @abstractmethod
    def clone(self,prog,f):
        pass
    
    @abstractmethod
    def evaluate(self,prog,f,sp :SelfPlay):
        pass