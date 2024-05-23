from pickle import FALSE
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

import psutil
class Test6:
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

        def test_aux(self,gs,utt,exi,f):
        
            #pgs = PhysicalGameState.load("../maps/basesWorkers32x32A.xml",utt);
            #pgs = PhysicalGameState.load("../maps/mapadavid2.xml",utt);
            #pgs = PhysicalGameState.load("../maps/BWDistantResources32x32.xml",utt)
           
            
            #gs2 = gs
         
            gs2 = GameState(gs)
          
            pgs = gs2.getPhysicalGameState()
            ai0 = CombatRush(pgs,utt,"Light")
            ai1 = CombatRush(pgs,utt,"Heavy")
            if exi :
                screen = ScreenMicroRTS(gs2)
            cont = 0
            show = False;
            
            print(pgs.getWidth())
            while not gs2.gameover() and cont<3000:
                
                screen.draw()
                if show and exi   :
                    screen.draw()
                    time.sleep(0.1) 
                
                #print("jogador0")
                
                time.sleep(100) 
                pa0 = ai0.getActions(gs2,0)
                #print("jogador1")
                if gs2.getTime()  == 0 and False:
                    f.write(str(gs2.getTime())+"\n")
                    for a in pgs.getUnits(0).items():
                        f.write(str(a[1].getNextID0())+"\n") 
                      
                        
                
                   
                pa1 = ai1.getActions(gs2,1)
                
              
                show = gs2.updateScream()
              
                gs2.issueSafe(pa0)
        
                gs2.issueSafe(pa1)
                
                
               # gs2.cycle()
          
                
                cont+=1;
            
            return " win ="+str( gs2.winner()) +" "+str(gs2.getTime())
           
            
            
       
        def test(self,map,arg):
            utt = UnitTypeTable(2);
            pgs = PhysicalGameState.load(map,utt)
            gs = GameState(pgs,utt)
            f = open('file'+arg+'.txt', 'w')
            f.close()
            process = psutil.Process()
            ant = process.memory_info().rss/(1024*1024) # in bytes 
            ini = time.time()
            for i in range (10000000):
                f = open('file'+arg+'.txt', 'a')
                ini0 = time.time()
                f.write("cont " +str(i)+self.test_aux(gs, utt,True,f))
                f.write("\n")
                fim = time.time()
                f.write("TempoP "+str(fim-ini0)+"\n")
                f.write("TempoT "+str(fim-ini)+"\n")
                process = psutil.Process()
                alt = process.memory_info().rss/(1024*1024)
                f.write("memoA "+str(alt))  # in bytes 
                f.write("\n")
                f.write("memoD "+str(alt-ant))  # in bytes 
                ant = alt
                f.write("\n")
                f.write("\n")
                f.close()
                
                     
               
                

        