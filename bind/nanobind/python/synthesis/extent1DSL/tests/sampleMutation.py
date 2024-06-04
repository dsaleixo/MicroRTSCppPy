

import random

from MicroRTS_NB import GameState, PhysicalGameState, UnitTypeTable
from selfPlay.selfPlayDefault import SelfPlayDefault
from synthesis.ai.Interpreter import Interpreter
from synthesis.baseDSL.tests.scriptsToy import ScriptsToy
from synthesis.baseDSL.util.control import Control
from synthesis.extent1DSL.extent1Main.s_E1 import S_E1
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class SampleMutation():
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def test0():
        for i in range(1000):
            s = S_E1()
            r = random.randint(1,10)
            s.sample(r)
            print(r,s.translate())
    
    @staticmethod
    def test1():
        for i in range(10):
            s = S_E1()
            s.sample(10)
            print("xxxxxxxxxxxxxxxxxxxx")
            print(s.translate())
            for j in range(2000):
                r = random.randint(1,4)
                l = []
                s.countNode(l)
                
                l[random.randint(0,len(l))-1].mutation(r)
                
            print(r,s.translate())
            print("\n\n\n")
            
    @staticmethod
    def test2():
        map = "maps/basesWorkers24x24A.xml"
        max_tick = 3000

        utt = UnitTypeTable(2)
        
        pgs = PhysicalGameState.load(map,utt)
        gs = GameState(pgs,utt)
        f = Factory_E1()
        s_empty = ScriptsToy.scriptEmpty()
        
        sp = SelfPlayDefault(s_empty,1)
        prog_current = sp.getBest().clone(f)
        score_current = sp.evaluate(prog_current,gs,max_tick)
        print(score_current,prog_current.translate())
     
        while True:
            
            for _ in range(30):
                print()
                
                mutation = prog_current.clone(Factory_E1())
                l = []
                mutation.countNode(l)
                #print(mutation.translate())
                #print(Control.save(mutation))
                no = l[0]
                #print(Control.save(no))
                no.mutation(15)
                #print(Control.save(no))
               # print(mutation.translate())
                score = sp.evaluate(mutation,gs,max_tick)
                print("xxxxxxs")
                print(prog_current.translate())
                print(str(score)+" "+str(score_current), mutation.translate())
                if score>score_current:
                    print("best ",mutation.translate())
                    
                    mutation.clear(None,Factory_E1())
                    print("clean ",mutation.translate())
                    prog_current =mutation.clone(Factory_E1())
                    sp.update(mutation)
                    score_current = sp.evaluate(mutation,gs,max_tick)
            
        
         