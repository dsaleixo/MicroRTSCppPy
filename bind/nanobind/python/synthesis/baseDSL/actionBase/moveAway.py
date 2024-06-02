from MicroRTS_NB import GameState, Unit
from synthesis.ai.Interpreter import Interpreter
from synthesis.baseDSL.almostTerminal.targetPlayer import TargetPlayer
from synthesis.baseDSL.mainBase.c import C, ChildC
from synthesis.baseDSL.mainBase.node import Node
from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy


from synthesis.baseDSL.util.factory import Factory



class MoveAway(ChildC,Node):
    
    def __init__(self) -> None:
        self._used = False
        pass
        
  
    
    def translate(self) -> str:
        return "u.moveAway()"
    
    def translate2(self) -> str:
        return "u.moveAway()"
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs + "u.moveAway()"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        gs2 = gs.clone()
        pgs = gs2.getPhysicalGameState()
        if u.getType().canMove and u.getPlayer()==player and automata._memory[u.getId()]  :
            u2 = automata.farthestAllyBase(pgs,player,u)
            if(u2!=None) :
                pf =  automata._core.pf
                move = pf.findPathToPositionInRange2(u, u2.getX() + u2.getY() * pgs.getWidth(),1, gs2 )
                if  move!=None :
                    self._used = True
                    automata._core.move(u, move.m_a, move.m_b)
                    automata._memory[u.getId()] = False
					
					
    def load(self, l : list[str], f :Factory):
        pass
	

    def save(self, l : list[str]):
        l.append("MoveAway")
        
    def clone(self, f : Factory) -> Node:
        return f.build_MoveAway()
    
    def resert(self, f : Factory) -> None:
        self._used = False
        
    def clear(self,father:Node, f : Factory) -> Node:
        return self._used
         
	
   
        
