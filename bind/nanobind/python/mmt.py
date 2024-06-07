import os
import glob
import time
from datetime import datetime

import torch
import torch.nn as nn
from torch.distributions import MultivariateNormal
from torch.distributions import Categorical

import numpy as np



############################## Environment Imports ##############################
from MicroRTS_NB import UnitType
from MicroRTS_NB import  UnitTypeTable
from MicroRTS_NB import GameState
from MicroRTS_NB import PhysicalGameState
from MicroRTS_NB import PlayerAction
from MicroRTS_NB import UnitAction
from MicroRTS_NB import Unit
from MicroRTS_NB import UnitActionAssignment
from MicroRTS_NB import AStarPathFinding
from util.screen import ScreenMicroRTS
from ai.rush.CombatRush import CombatRush


map = "maps/map_1.xml"
#map = "maps/basesWorkers24x24A.xml"
utt = UnitTypeTable(2); 

gs = GameState(map,utt)
pgs = gs.getPhysicalGameState()
show = True;
num = 0

while(num<50):
    #map = "maps/basesWorkers24x24A.xml"
    map = "./maps/map_%s.xml"%(num+1)
    cont2 =0
    while cont2 <= 50:
        cont2+=1
        
        gs2 = GameState(map,utt)
        pgs2 = gs2.getPhysicalGameState()
        print("error happens here")
        pgs2 = PhysicalGameState.load(map ,utt)

        ai0 = CombatRush(pgs2, utt, "Ranged") 
        ai1 = CombatRush(pgs2, utt, "Heavy") 
        #screen = ScreenMicroRTS(gs2)
        gameover = False
        cont=0

        current_ep_reward = 0
        while (not gs2.gameover()) and cont<10: # run one epiosod

            pa0 = ai0.getActions(gs2,0) #TODO: extend for multi unit, the output might be a list??
            pa1 = ai1.getActions(gs2,1)
  
            gs2.issueSafe(pa0) #if it is not legal action, assignes it with a none action of the same duratoion
            gs2.issueSafe(pa1)
            #show = gs2.updateScream()
            gs2.cycle() #like env.step -> state, reward, done, _ = env.step(action) -- new state is just the new gs2 (automatically updated)
            cont += 1

           
           
        print("win = ",gs2.winner())
        print(cont)
        # if gs2.winner() == 0:
        #     input("YAY")

    num += 1




# print total training time
print("============================================================================================")
end_time = datetime.now().replace(microsecond=0)
print("Started training at (GMT) : ", start_time)
print("Finished training at (GMT) : ", end_time)
print("Total training time  : ", end_time - start_time)
print("============================================================================================")