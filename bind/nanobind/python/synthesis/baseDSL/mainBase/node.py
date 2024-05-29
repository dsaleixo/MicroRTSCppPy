from __future__  import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from MicroRTS_NB import Unit
    from MicroRTS_NB import GameState
    from synthesis.ai.Interpreter import Interpreter

from abc import ABC, abstractmethod





class Node(ABC):
    @abstractmethod
    def translate(self) -> str:
        pass
    
    @abstractmethod
    def  translateIndentation(self,n_tab:int) ->str:
        pass
    
    @abstractmethod
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        pass
	
    @classmethod
    def getName(cls)->str:
        return cls.__name__
        

	