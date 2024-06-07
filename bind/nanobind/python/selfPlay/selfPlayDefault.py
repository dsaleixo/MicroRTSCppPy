


from inspect import _void
from ai.ai import AI
from playout.simpleMatch import SimpleMatch
from selfPlay.selfPlay import SelfPlay
from synthesis.ai.Interpreter import Interpreter
from synthesis.baseDSL.mainBase.for_S import For_S
from synthesis.baseDSL.mainBase.node import Node
from synthesis.extent1DSL.extent1Main.empty_E1 import Empty_E1
from synthesis.extent1DSL.extent1Main.s_E1 import S_E1

from MicroRTS_NB import GameState, UnitTypeTable

class SelfPlayDefault(SelfPlay):
    
    def __init__(self,n:int):
        self._n : int = n
        self._progs : list[Node] = []
        self._sm = SimpleMatch()
       
        self._n_count = 0
       
        
        
    def getN(self):
        return self._n_count
  
    def update(self, prog : Node)-> None:
        if self._n == len(self._progs):
            p = self._progs.pop(0)
        
        self._progs.append(prog)
        
        
    

    def winToScore(self,player:int,result:int)->float:
        if player == result: return 1.0
        if 1 - player == result: return 0.0
        return 0.5

    def evaluate(self, node : Node, gs : GameState, max_tick :int)->float:
        pgs = gs.getPhysicalGameState()
        utt = gs.getUTT()
        a1 = Interpreter(gs.getPhysicalGameState(),utt,For_S(node))
        score = 0
        for n2 in self._progs:
            a2 = Interpreter(gs.getPhysicalGameState(),utt,For_S(n2))
            score += self.winToScore(0,self._sm.playout(gs,a1,a2,max_tick,False) )
            score += self.winToScore(1,self._sm.playout(gs,a2,a1,max_tick,False) )
            self._n_count += 1 
        return score/(2*len(self._progs))
    
    def getBest(self)->AI:
        return self._progs[-1]
    
    def getIndividual(self)->AI:
        return self.getBest()
    
 
    def stoppingCriterion(self,score)->False:
        if abs(1.0-score)< 0.001:
            return True
        return False