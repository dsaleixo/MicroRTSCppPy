


from synthesis.baseDSL.actionBase.idle import Idle
from synthesis.baseDSL.mainBase.node import Node


class Idle_E1(Idle):
    def __init__(self) -> None:
        self._used = False
        pass
    
    def sample(self):
        pass
    
         
    def countNode(self,l : list[Node]):
        pass
        
    def mutation(self,bugdet):
        self.sample()