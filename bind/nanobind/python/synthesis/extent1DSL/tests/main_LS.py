
import time
from MicroRTS_NB import GameState, PhysicalGameState, UnitTypeTable

import torch

from logger.stdout_logger import StdoutLogger
from selfPlay.selfPlayDefault import SelfPlayDefault
from synthesis.baseDSL.mainBase.node import Node
from synthesis.baseDSL.tests.scriptsToy import ScriptsToy
from synthesis.extent1DSL.LocalSearch.HC import HC
from synthesis.extent1DSL.LocalSearch.SA import SA

from synthesis.extent1DSL.LocalSearch.individuals.individual import Individual
from synthesis.extent1DSL.LocalSearch.individuals.individual_Default import Individual_Default

#from selfPlay.selfPlayDefault import SelfPlayDefault
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1
from synthesis.extent1DSL.mutation.mutation import Mutation
from synthesis.extent1DSL.mutation.mutation1 import Mutation1
from synthesis.extent1DSL.mutation.mutation0 import Mutation0



class MainSynthesis():
    
    def setMap(self):
        if self._opMap == "0": 
            self._map = "maps/basesWorkers24x24A.xml"
            self._time = 2000
            self._max_tick = 6000
        if self._opMap == "1": 
            self._map = "maps/basesWorkers32x32A.xml"
            self._time = 2000
            self._max_tick = 6000
        if self._opMap == "2": 
            self._map = "maps/BroodWar/(4)BloodBath.scmB.xml" 
            self._time = 4000
            self._max_tick = 15000
    
    def __init__(self,args):
        self._f = Factory_E1()
        self._opMap = args[1]
        self._opSearch = args[2]
        self._opIndividual= args[3]
        self._opSelfPlay = args[4]
        id_test = args[1] +"_"+ args[2] +"_"+ args[3] + "_"+args[4] + "_"+args[5]
        StdoutLogger.init_logger(id_test)
        StdoutLogger.log("id_conf",id_test)
        
        self.setMap()
        self.setIndividual()
        self.setSearch()
        self.setSelfplay()
    
    

    

    def setIndividual(self) -> Mutation:
        if self._opIndividual == "0": self._ind = Individual_Default( Mutation0())
        if self._opIndividual == "1": self._ind = Individual_Default( Mutation1())
        
    
    def setSearch(self):
        if self._opSearch == "0": self._search = HC()
        if self._opSearch == "1": self._search = SA(2000,0.9,0.5)
    def setSelfplay(self):
        if self._opSelfPlay == "0": self._selfPlay = SelfPlayDefault(1 ) #IBR
        if self._opSelfPlay == "1": self._selfPlay =  SelfPlayDefault(1000) # Ficticious


    
        
        
    def run(self):
        
        utt : UnitTypeTable= UnitTypeTable(2)
        
        pgs : PhysicalGameState = PhysicalGameState.load(self._map ,utt)
        gs : GameState= GameState(pgs,utt)
        
        s_empty :Node = ScriptsToy.scriptEmpty()
        
        self._selfPlay.update(s_empty)
        
        
        start_time = time.time()
        while True:
            
            prog = self._selfPlay.getIndividual().clone(self._f)
            r1 = self._selfPlay.evaluate(prog,gs,self._max_tick )
            prog_result, r0, log = self._search.run(prog,gs,self._selfPlay,self._ind,5,self._time,self._max_tick)
            
            if r0 > r1:
                time_eval = time.time() - start_time
                log +="Camp\t"+str(time_eval)+"\t"+str(self._selfPlay.getN())+"\t"+prog_result.translate()+"\n"
                self._selfPlay.update(prog_result.clone(self._f))
            
            
            
            StdoutLogger.log("search",log)

        
    @staticmethod
    def execute(args):
        main = MainSynthesis(args)
        main.run()
        



   

        