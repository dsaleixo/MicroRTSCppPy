from abc import ABC, abstractmethod

from synthesis.baseDSL.mainBase.node import Node

class Mutation(ABC):
    @abstractmethod
    def getMutations(self,prog, n_mutation) -> list[Node]:
        pass
    
    