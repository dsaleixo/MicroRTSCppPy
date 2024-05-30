import torch
#from InterfacePython import Match
#from ai import RandomBiasedAI
#from ai.evaluation import SimpleSqrtEvaluationFunction3
#from  ai.mcts.naivemcts import NaiveMCTS
#from ai.abstraction import HeavyRush
from MicroRTS_NB import PhysicalGameState, UnitAction, UnitTypeTable;
from MicroRTS_NB import Unit;
from MicroRTS_NB import GameState

from ai.rush.CombatRush import CombatRush
from util.screen import ScreenMicroRTS

import time

class GetInstance0():
    
    action_label = {"wait":0, "up":1, "down":3, "right":2, "left":4,
                    
                    (-2,-2):6,  (-2,-1):7,   (-2,0):8,  (-2,1):9,  (-2,2):10,
                    (-1,-2):11, (-1,-1):12,  (-1,0):13, (-1,1):14, (-1,2):15,
                    (0,-2) :16, (0,-1) :17,             (0,1) :18, (0,2) :19,
                    (1,-2) :20, (1,-1) :21, (1,0) :22,  (1,1) :23, (1,2) :24,
                    (2,-2) :25, (2,-1) :26, (2,0) :27,  (2,1) :28, (2,2) :29,
                    (0, 3) :30, (3,0) :31,            (0,-3) :32, (-3,0) :33,  
                    }
    
    label_action = {v: k for k, v in action_label.items()}
    
    @staticmethod
    def getAction(u : Unit, a : UnitAction)-> int:
        if a.getType() == 5:
            x = u.getX() - a.getLocationX()
            y = u.getY() - a.getLocationY()
            p = (x,y)
            
            return GetInstance0.action_label[p]
            
        elif a.getType() == 1:
            direc = GetInstance0.label_action[a.getDirection()+1]
            return GetInstance0.action_label[direc]
            
        elif a.getType() == 0:
            return 0
    
    
    @staticmethod
    def StateToInput(gs: GameState)->torch.Tensor:
        input = torch.zeros([2, 8,8], dtype=torch.float)
        pgs = gs.getPhysicalGameState()
        for u2 in pgs.getUnits(0).values():
            x = u2.getX()
            y = u2.getY()
            if u2.getPlayer()==0:input[0,y,x]=1
            else :
                
                input[0,y,x]=-1
                
                uaa = gs.getActionAssignment(u2)
                t = gs.getTime()
                if uaa != None:
                    t = uaa.time + uaa.action.ETA(uaa.unit)
                
                input[1,y,x]= (t - gs.getTime())/12
        for u2 in pgs.getUnits(1).values():
            x = u2.getX()
            y = u2.getY()
            if u2.getPlayer()==0:input[0,y,x]=1
            else :
                
                input[0,y,x]=-1
                
                uaa = gs.getActionAssignment(u2)
                t = gs.getTime()
                if uaa != None:
                    t = uaa.getTime() + 10 # uaa.getUnitAction().ETA(uaa.getUnit())
                
                input[1,y,x]= (t - gs.getTime())/12
            
        return input
    @staticmethod
    def generate(): # -> (torch.Tensor, torch.Tensor): 
        input = []
        output = []
        map = "./maps/map0.xml"
        max_tick = 3000
        show_scream = True
      
        utt = UnitTypeTable(2);
        pgs = PhysicalGameState.load(map,utt)
        gs = GameState(pgs,utt)
        ai0 =  CombatRush(pgs,utt,"Ranged")
        ai1 = CombatRush(pgs,utt,"Heavy")
        
        screen = ScreenMicroRTS(gs)
        cont = 0
        show = True;
        
        gameover = False
        
        while (not gs.gameover()) and gs.getTime()<max_tick:
            
            if show :
                    screen.draw()
                    time.sleep(0.1) 

            pa0 = ai0.getActions(gs,0)
            pa1 = ai1.getActions(gs,1)
            for ua in pa0.getActions().values():
                print(ua[0].toString(), ua[1].toString())
                aa =int(GetInstance0.getAction(ua[0],ua[1]))
                input.append(GetInstance0.StateToInput(gs))
                
                output.append(aa)
            show = gs.updateScream()
            gs.issueSafe(pa0)
            gs.issueSafe(pa1)
            gs.cycle()
        if show :
            screen.draw()
            time.sleep(0.1) 
        
        inp = torch.stack(input)
        
        out = torch.Tensor(output)
        out = out.to(torch.long)
        print("ee")
        print(inp.shape,out.shape)
        return inp, out
    @staticmethod
    def test():
        inp, output = GetInstance0.generate()   
        print("ee")
        print(inp.shape,output.shape)
        
    
        