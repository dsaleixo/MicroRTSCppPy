from .AbstractAction import AbstractAction
from MicroRTS_NB import GameState, Unit,UnitAction,ResourceUsage

class Idle(AbstractAction):
    

    def toString(self):
        return "idle todo "

    def __init__(self, u : Unit) :
        super().__init__(u)
    
    
    def completed(self, gs : GameState)->bool:
        return False
    
    
    #public boolean equals(Object o)
   

    
    #public void toxml(XMLWriter w)            

    def execulte(self, gs : GameState,  ru : ResourceUsage)->UnitAction :
        pgs = gs.getPhysicalGameState();
       
        if  not self._unit.getType().getCanAttack(): return None;
        for target in pgs.getUnits(1-self._unit.getPlayer()).values() :
            
                dx = target.getX()-self._unit.getX();
                dy = target.getY()-self._unit.getY();
                d = (dx*dx+dy*dy)**0.5;
                if d<=self._unit.getAttackRange():
                    return  UnitAction(UnitAction.getTYPE_ATTACK_LOCATION(),target.getX(),target.getY());
           
        return None;
    
    
    
    