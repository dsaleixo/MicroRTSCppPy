import sys
sys.path.append("../..")
sys.path.append("../")
from xml.etree.ElementTree import tostring

from ai.abstraction.AbstractionLayerAI import AbstractionLayerAI
from ai.rush.CombatRush import CombatRush

from MicroRTS_NB import  UnitTypeTable
from MicroRTS_NB import PhysicalGameState
from MicroRTS_NB import UnitType
from MicroRTS_NB import GameState
from MicroRTS_NB import PlayerAction
from MicroRTS_NB import UnitAction
from MicroRTS_NB import Unit
from MicroRTS_NB import UnitActionAssignment
from MicroRTS_NB import AStarPathFinding


import random

from util.screen import ScreenMicroRTS

import time

from memory_profiler import profile
import objgraph 
import psutil
process = psutil.Process()
print(process.memory_info().rss)  # in bytes 
class Test5:
        def __init__(self):
            pass 

        
        def test_aux0(self,map,utt):
            
            #pgs = PhysicalGameState.load("../maps/basesWorkers32x32A.xml",utt);
            #pgs = PhysicalGameState.load("../maps/mapadavid2.xml",utt);
            #pgs = PhysicalGameState.load("../maps/BWDistantResources32x32.xml",utt)
           
            pgs = PhysicalGameState.load(map,utt)
            gs = GameState(pgs,utt)
            ai0 = CombatRush(pgs,utt,"Light")
            ai1 = CombatRush(pgs,utt,"Heavy")

        def test_aux(self,map):
            utt = UnitTypeTable(2);
            #pgs = PhysicalGameState.load("../maps/basesWorkers32x32A.xml",utt);
            #pgs = PhysicalGameState.load("../maps/mapadavid2.xml",utt);
            #pgs = PhysicalGameState.load("../maps/BWDistantResources32x32.xml",utt)
           
            pgs = PhysicalGameState.load(map,utt)
            
            gs = GameState(pgs,utt)
            ai0 = CombatRush(pgs,utt,"Light")
            ai1 = CombatRush(pgs,utt,"Heavy")
            
            #screen = ScreenMicroRTS(gs)
            cont = 0
            show = False;
            
           
            while not gs.gameover() and cont<3000:
                
                #print(gs.getTime())
                #if show :
                #    screen.draw()
                #    time.sleep(0.1) 
                #print("jogador0")
             
                pa0 = ai0.getActions(gs,0)
                #print("jogador1")
                
                
                   
                pa1 = ai1.getActions(gs,1)
                
              
                show = gs.updateScream()
              
                gs.issueSafe(pa0)
        
                gs.issueSafe(pa1)
             
              
                gs.cycle()
          
                
                cont+=1;
            print("win =", gs.winner(),gs.getTime())
           
            
            
       
        def test(self,map):
            
            
            for i in range (10000):
                print("cont",i)
                self.test_aux(map)
                process = psutil.Process()
                print("memo ",process.memory_info().rss)  # in bytes 
            objgraph.show_most_common_types(limit=20)       
                     
               
                

        