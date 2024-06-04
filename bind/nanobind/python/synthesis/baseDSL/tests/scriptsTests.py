from synthesis.baseDSL.tests.scriptsToy import ScriptsToy
from synthesis.baseDSL.util.control import Control
from synthesis.baseDSL.util.factory_Base import Factory_Base
from synthesis.ai.Interpreter import Interpreter
from MicroRTS_NB import GameState, PhysicalGameState, UnitTypeTable
from playout.simpleMatch import SimpleMatch
class ScriptsTests(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def test0():
        script = ScriptsToy.scriptEmpty()
        script0 = ScriptsToy.script6()
        print(script.translate())
        map = "./maps/basesWorkers32x32A.xml"
        utt = UnitTypeTable(2)
        
        pgs = PhysicalGameState.load(map,utt)
        gs = GameState(pgs,utt)
        print(script0.translate())
        ai = Interpreter(pgs,utt,script)
       
        ai1 = Interpreter(pgs,utt,script0)


        
        sm = SimpleMatch()
        win = sm.playout(gs,ai1,ai,7000,True)
        print("win =",win)
        #script.clear(None,Factory_E1())
        print(script.translate())


        
    @staticmethod
    def test1():
        s0 = ScriptsToy.script0()
        s1 = ScriptsToy.script1()
        s2 = ScriptsToy.script2()
        s3 = ScriptsToy.script3()
        s4 = ScriptsToy.script4()
        s5 = ScriptsToy.script5()
        s6 = ScriptsToy.script6()
        scripts = [s1, s2, s3, s4, s5,s0,s6]
        f = Factory_Base()
        for s in scripts:
            print(s.translate())
            trace = Control.save(s)
            print(trace)
            new = Control.load(trace,f)
            print(new.translate())
            print()
            print()
        
    
