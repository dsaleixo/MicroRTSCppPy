from __future__  import annotations
from typing import TYPE_CHECKING

from MicroRTS_NB import GameState


if TYPE_CHECKING:
    from synthesis.ai.Interpreter import Interpreter




class Memory:
    
    def __init__(self, gs : GameState,player :int, automata :Interpreter):
        self._freeUnit = {}
        pgs = gs.getPhysicalGameState()
        for u2 in pgs.getUnits(player).values():
            if  automata._core.getAbstractAction(u2)==None:
                pass
                #print(u2.toString(),"None")
            else:
                print(u2.toString(),automata._core.getAbstractAction(u2).toString())
            self._freeUnit[u2.getID()] = automata._core.getAbstractAction(u2) == None