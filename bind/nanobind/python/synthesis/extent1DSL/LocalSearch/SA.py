


import math
import random

from MicroRTS_NB import GameState

from selfPlay.selfPlay import SelfPlay
from synthesis.extent1DSL.LocalSearch.individuals.individual import Individual
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1

import time

class SA:
    
    def __init__(self,T0 : float, alpha : float, beta :float):
        self._T0 = T0
        self._T = T0
        self._alpha = alpha
        self._beta = beta
        self._f = Factory_E1()
        pass
    
    def accept(self,score_local,best_score_neighborhood):
        aux2 = math.exp(self._beta*((best_score_neighborhood - score_local)/self._T))
        aux2 = min(1,aux2)  
        if random.random()<aux2:
            return True
		
        return False
    
    def run(self, prog, gs : GameState, sp : SelfPlay, ind_handler : Individual,n_neighborhood:int, max_time : int,max_tick :int):
        log = ""
        ind = ind_handler.progToInd(prog)
        self._T0 = self._T0
        start_time = time.time()
        
        score_best=score_local = ind_handler.evaluate(ind,gs,max_time,self._f,sp)
        ind_local = ind_handler.clone(ind,self._f)
        time_eval = time.time() - start_time
        print("actual\t"+str(time_eval)+"\t"+str(time_eval)+"\t"+str(sp.getN())+"\t"+str(score_local)+"\t"+ind_handler.toString(ind)+"\n")
        log +="actual\t"+str(time_eval)+"\t"+str(time_eval)+"\t"+str(sp.getN())+"\t"+str(score_local)+"\t"+ind_handler.toString(ind)+"\n"
        count = 0
        while True:
            self._T = self._T0/(1+count*self._alpha)
            mutations = ind_handler.getNeighborhood(ind_local,n_neighborhood)
            print(mutations[0].translate())
           
            best_score_neighborhood = ind_handler.evaluate(mutations[0],gs,max_time,self._f,sp)
           
            
            best_ind_neighborhood = mutations[0]
            for i  in  range(1,n_neighborhood):
                start_time2 = time.time()
                result = ind_handler.evaluate(mutations[i],gs,max_time,self._f,sp)
                time_eval2 = time.time() - start_time2
                time_eval3 = time.time() - start_time
                print("actual\t"+str(time_eval3)+"\t"+str(time_eval2)+"\t"+str(sp.getN())+"\t"+str(result)+"\t"+ind_handler.toString(mutations[i])+"\n")
                log += "actual\t"+str(time_eval3)+"\t"+str(time_eval2)+"\t"+str(sp.getN())+"\t"+str(result)+"\t"+ind_handler.toString(mutations[i])+"\n"
                time_eval = time.time() - start_time
                if result > best_score_neighborhood:
                    
                    best_score_neighborhood = result
                    best_ind_neighborhood = mutations[i]
              
              
            if self.accept(score_local,best_score_neighborhood):
                score_local = best_score_neighborhood
                ind_local = best_ind_neighborhood
            
            if best_score_neighborhood > score_best:
                
                log+="actual2\t"+ind_handler.toString(best_ind_neighborhood)+"\n"
                score_best = best_score_neighborhood
                ind = best_ind_neighborhood
            
            count +=1
            end_time = time.time()
            
            
            if end_time - start_time > max_time or sp.stoppingCriterion(score_best):
                break
        return ind_handler.indToProg(ind), score_best, log
        