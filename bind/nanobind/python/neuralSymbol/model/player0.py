import torch


from neuralSymbol.model.Model0 import Model0
from neuralSymbol.model.getInstance0 import GetInstance0
from MicroRTS_NB import PhysicalGameState, UnitAction;
from MicroRTS_NB import Unit;
from MicroRTS_NB import GameState
from MicroRTS_NB import UnitTypeTable
from ai.rush.CombatRush import CombatRush
from MicroRTS_NB import PlayerAction

from util.screen import ScreenMicroRTS

import time

class Player0:
    
    def __init__(self):
        self.model = Model0()
        self.model.load_state_dict(torch.load("./neuralSymbol/model/models/model0.pt"))
        
    def crateAction(self,i :int, u : Unit)->UnitAction:
        if i==0:
            return UnitAction(0,10)
        elif i<5:
            return UnitAction(1,i-1)
        else:
            x,y =  GetInstance0.label_action[i]
            
            
            return UnitAction(5,u.getX()-x,u.getY()-y)
        
        
    def getActions(self,gs : GameState,player : int) -> PlayerAction:
        pa = PlayerAction()
        pgs = pgs = gs.getPhysicalGameState()
        for u in pgs.getUnits(player).values():
            if gs.getActionAssignment(u)==None:
                input = GetInstance0.StateToInput(gs).unsqueeze(dim=0)
                output = self.model(input)
                a = self.crateAction(output.argmax().item(),u)
                pa.addUnitAction(u,a)
    
                
        
        return pa
        
    def reset(self,utt : UnitTypeTable ):
        pass
    
    @staticmethod
    def test():
       
        map = "./maps/map0.xml"
        max_tick = 3000
        show_scream = True
      
        utt = UnitTypeTable(2);
        pgs = PhysicalGameState.load(map,utt)
        gs = GameState(pgs,utt)
        
        ai0 = Player0()
        screen = ScreenMicroRTS(gs)
        show = True;
        cont=0
        ai1 = CombatRush(pgs,utt,"Heavy")
       
        
        gameover = False
      
        while (not gs.gameover()) and cont<3000:
            if show :
                    screen.draw()
                    time.sleep(0.5) 
            
            pa0= ai0.getActions( gs,0)
            for a in pa0.getActions().values():
                    print(a[0].toString(), a[1].toString())
            pa1 =ai1.getActions( gs,1)
            
            gs.issueSafe(pa0)
            gs.issueSafe(pa1)
            show = gs.updateScream()
            gs.cycle()
            cont+=1
        
        print("win = ",gs.winner())
        