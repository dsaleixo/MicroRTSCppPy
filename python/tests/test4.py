import sys
sys.path.append("../..")
sys.path.append("../")
from xml.etree.ElementTree import tostring

from ai.abstraction.AbstractionLayerAI import AbstractionLayerAI
from ai.rush.CombatRush import CombatRush

from MicroRTSpy import  UnitTypeTable
from MicroRTSpy import PhysicalGameState
from MicroRTSpy import UnitType
from MicroRTSpy import GameState
from MicroRTSpy import PlayerAction
from MicroRTSpy import UnitAction
from MicroRTSpy import Unit
from MicroRTSpy import UnitActionAssignment
from MicroRTSpy import AStarPathFinding


import random

from util.screen import ScreenMicroRTS

import time

class Test4:

        @staticmethod
        def test(map):
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
            inicio = time.time()
            tempo0=0
            tempo1=0
            tempo2=0
            while not gs.gameover() and gs.getTime()<3000:
                #print("time ",cont)   
                #if show :
                #    screen.draw()
                #    time.sleep(0.1) 
                #print("jogador0")
                inicio = time.time()
                pa0 = ai0.getActions(gs,0)
                #print("jogador1")
            
                pa1 = ai1.getActions(gs,1)
                fim = time.time()
                tempo0+=fim - inicio
                #show = gs.updateScream()
                inicio = time.time()
                gs.issueSafe(pa0)
                gs.issueSafe(pa1)
                fim = time.time()
                tempo1+=fim - inicio
                inicio = time.time()
                gs.cycle()
                fim = time.time()
                
                tempo2+=fim - inicio
                cont+=1;
            print(ai0._t4,ai0._t0,ai0._t1,ai0._t2,ai0._t3,ai1._t0,ai1._t1,ai0._t2,ai0._t3)
            print("T ",tempo0,tempo1,tempo2, tempo0+tempo1+tempo2)
            print("winner = ", gs.winner(), gs.getTime())


                

        