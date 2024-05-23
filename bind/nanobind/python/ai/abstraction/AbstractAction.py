
from MicroRTS_NB import Unit
from MicroRTS_NB import GameState
from MicroRTS_NB import UnitAction
from MicroRTS_NB import ResourceUsage


class AbstractAction:
    
    def __init__(self, u : Unit):
        self._unit = u
        
    def toString(self):
        pass

    def  getUnit(self) -> Unit:
        return self._unit
    
    
    def setUnit(self, u : Unit) -> None:
        self._unit = u
    
    
    def completed(self, pgs : GameState) -> bool:
        pass
    
    
    def execute(self, pgs : GameState):
        return self.execute(pgs,None)
    


    #def toxml(XMLWriter w);
    
    
    #def fromXML(Element e, PhysicalGameState gs, UnitTypeTable utt)
    
    
    
    def execute(self, pgs : GameState,  ru : ResourceUsage)->UnitAction:
        pass
        