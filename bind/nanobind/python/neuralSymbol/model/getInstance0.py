import torch
#from InterfacePython import Match
#from ai import RandomBiasedAI
#from ai.evaluation import SimpleSqrtEvaluationFunction3
#from  ai.mcts.naivemcts import NaiveMCTS
#from ai.abstraction import HeavyRush
from MicroRTS_NB import UnitAction;
from MicroRTS_NB import Unit;
from MicroRTS_NB import GameState

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
        path = "maps/newMaps/map0.xml"
        max_tick = 3000
        show_scream = False
        mch = Match(path, show_scream)
        ai0 =  NaiveMCTS(100, -1, 100,10,0.3, 1.0, 0.0, 1.0, 0.4, 1.0,  RandomBiasedAI(),  SimpleSqrtEvaluationFunction3(),False)
        
        ai1 = HeavyRush(mch.getUTT())
        
        ai0.reset(mch.getUTT())
        ai1.reset(mch.getUTT())
        
        gameover = False
        
        while (not gameover) and mch.getGS().getTime()<max_tick:
            pa0= ai0.getAction(0, mch.getGS())
            pa1 =ai1.getAction(1, mch.getGS())
            for ua in pa0.getActions():
                aa =int(GetInstance0.getAction(ua.m_a,ua.m_b))
                input.append(GetInstance0.StateToInput(mch.getGS()))
                
                output.append(aa)
                
            mch.SetActions(pa0)
            mch.SetActions(pa1)
            gameover = mch.run()
        mch.run()
        inp = torch.stack(input)
        
        out = torch.Tensor(output)
        out = out.to(torch.long)
        return inp, out
    @staticmethod
    def test():
        input, output = GetInstance0.generate()   
        print(input.shape,output.shape)
        
    
        