from __future__  import annotations
from typing import TYPE_CHECKING








if TYPE_CHECKING:
   from synthesis.baseDSL.mainBase.Node import Node


from MicroRTS_NB  import UnitType, UnitTypeTable
from MicroRTS_NB import Unit

from MicroRTS_NB import GameState
from MicroRTS_NB import PlayerAction
from MicroRTS_NB import Player,PhysicalGameState


from ai.abstraction.AbstractionLayerAI import AbstractionLayerAI



class Interpreter:
    
    def __init__(self,utt : UnitTypeTable, n : Node) -> None:
        self._n : Node = n
        self._utt : UnitTypeTable = utt
        self._core  : AbstractionLayerAI= AbstractionLayerAI(utt)
        self.resource :int = None
        self.workerType : UnitType = utt.getUnitType("Worker")
        self.baseType : UnitType= utt.getUnitType("Base")
        self.barracksType : UnitType = utt.getUnitType("Barracks")
        self.rangedType : UnitType = utt.getUnitType("Ranged")
        

        
    def reset(self,utt : UnitTypeTable):
        self._utt = utt
        self._core = AbstractionLayerAI(utt)
        self.workerType = utt.getUnitType("Worker")
        self.baseType = utt.getUnitType("Base")
        self.barracksType = utt.getUnitType("Barracks")
        self.rangedType = utt.getUnitType("Ranged")
        
    def getAction(self, player:int,  gs:GameState) -> PlayerAction:
        self.resource = gs.getPlayer(player).getResources()
        #self._core.clear()
        #self._memory = Memory(gs,self)
        self._n.interpret(gs, player,None, self)
        return self._core.translateActions(player, gs)
        
        
        
        
    '''    
    def  farthestAllyBase(self, pgs: PhysicalGameState, player: int,  unitAlly : Unit) ->Unit :

        farthestBase = None
        farthesttDistance = 0
        for  u2 in pgs.getUnits():
            if (u2.getType().name == "Base"):

                if (u2.getPlayer() >= 0 and u2.getPlayer() == player) :
                    d = abs(u2.getX() - unitAlly.getX()) + abs(u2.getY() - unitAlly.getY());
                    if farthestBase == None or d > farthesttDistance:
                        farthestBase = u2
                        farthesttDistance = d
     
        return farthestBase
        
        
    def countHarvester(self, player:int,  gs:GameState):
        pgs = gs.getPhysicalGameState()
        cont =0
    	
    	
        for  u2 in pgs.getUnits():
            if   u2.getPlayer() == player :
                a2 = self._core.getAbstractAction(u2)
                if isinstance(a2 , ai.abstraction.Harvest) :
                    cont+=1

        return cont
        
        
        
        
    def countUnit(self,type, player:int,  gs:GameState):
        count =0
        pgs = gs.getPhysicalGameState()
        for u2 in pgs.getUnits():
            if u2.getPlayer()==player and u2.getType().name == type:
                count+=1
        return count
    
    def countConstrution(self,typeU, player:int,  gs:GameState):
        cont=0
        pgs = gs.getPhysicalGameState()
        for u2 in pgs.getUnits():
            if u2.getPlayer()==player:
                if u2.getType().name == typeU:
                    cont+=1
                elif u2.getType().name == "Worker":
                    a2 = self._core.getAbstractAction(u2)
                    aux=False
                    
                    if  isinstance(a2,ai.abstraction.Build)  :
                        
                        if a2.type.name==typeU:
                            aux=True	
                    if aux:
                        cont+=1
        return cont
    
    
    
    def countTrain(self,typeU, player:int,  gs:GameState):
        cont=0
        pgs = gs.getPhysicalGameState()
        for u2 in pgs.getUnits():
            if u2.getPlayer()==player:
                if u2.getType().name == typeU:
                    cont+=1
                elif u2.getType().name == "Barracks" or u2.getType().name == "Base":
                    a2 = self._core.getAbstractAction(u2)
                    aux=False
                    
                    if  isinstance(a2,ai.abstraction.Train)  :
                        
                        if a2.type.name==typeU:
                            aux=True
                            
                            	
                    if aux:
                        cont+=1
        return cont
    
                
    def getUnitClosest(self,gs : GameState, p : Player, u : Unit) -> Unit:
        pgs = gs.getPhysicalGameState()
        closestEnemy = None
        closestDistance = 0
        for  u2 in pgs.getUnits():
            if u2.getPlayer() >= 0 and u2.getPlayer() != p.getID() and u.getID() != u2.getID() :
                d = abs(u2.getX() - u.getX()) + abs(u2.getY() - u.getY())
                if closestEnemy == None or d < closestDistance:
                    closestEnemy = u2
                    closestDistance = d
                
        return closestEnemy
    
    def getUnitFarthest(self,gs : GameState, p : Player, u : Unit) -> Unit:
        pgs = gs.getPhysicalGameState()
        FarthestEnemy = None
        FarthestDistance = 1000000
        for u2 in pgs.getUnits():
            if u2.getPlayer() >= 0 and u2.getPlayer() != p.getID() and u.getID() != u2.getID():
                d = abs(u2.getX() - u.getX()) + abs(u2.getY() - u.getY())
                if FarthestEnemy == None or d > FarthestDistance:
                    FarthestEnemy = u2
                    FarthestDistance = d
        return FarthestEnemy
	
    def getUnitLessHealthy(self,gs : GameState, p : Player, u : Unit) -> Unit:
    
        pgs = gs.getPhysicalGameState()
        closestHealthy = None
        closestDistance = 0
        Healthy = 10000
        
        for   u2 in pgs.getUnits():
            if u2.getPlayer() >= 0 and u2.getPlayer() != p.getID() and u.getID() != u2.getID():
                d = abs(u2.getX() - u.getX()) + abs(u2.getY() - u.getY())
                if closestHealthy == None  or  Healthy > u2.getMaxHitPoints():
                    Healthy = u2.getMaxHitPoints()
                    closestHealthy = u2
                    closestDistance =d
                elif Healthy == u2.getMaxHitPoints() :
	            	
                    if closestHealthy == None or d < closestDistance:
                        Healthy = u2.getMaxHitPoints()
                        closestHealthy = u2
                        closestDistance =d
        return closestHealthy   
	
 
    def getUnitStrongest(self,gs : GameState, p : Player, u : Unit) -> Unit:
    
        pgs = gs.getPhysicalGameState()
        closestStrongest = None
        closestDistance = 0
        Strongest = -1
        
        
        for  u2 in pgs.getUnits():
            if u2.getPlayer() >= 0 and u2.getPlayer() != p.getID() and u.getID() != u2.getID():
                d = abs(u2.getX() - u.getX()) + abs(u2.getY() - u.getY())
                if closestStrongest == None or Strongest < u2.getMaxDamage():
                    Strongest = u2.getMaxDamage()
                    closestStrongest = u2
                    closestDistance =d
            	
                elif Strongest == u2.getMaxDamage():
	            	
                    if (closestStrongest == None or d < closestDistance) :
                        closestStrongest = u2
                        closestDistance = d
                        Strongest = u2.getMaxDamage()
	                
         
        return closestStrongest
	
 
 
    def getUnitMostHealthy(self,gs : GameState, p : Player, u : Unit) -> Unit:
    
        pgs = gs.getPhysicalGameState()
        closestHealthy = None
        closestDistance = 0
        Healthy = 0
    
        for  u2 in pgs.getUnits() :
            if u2.getPlayer() >= 0 and u2.getPlayer() != p.getID() and u.getID() != u2.getID():
                d = abs(u2.getX() - u.getX()) + abs(u2.getY() - u.getY())
                if closestHealthy == None or Healthy < u2.getMaxHitPoints():
                    Healthy = u2.getMaxHitPoints()
                    closestHealthy = u2
                    closestDistance =d
                elif Healthy == u2.getMaxHitPoints() :
                    if (closestHealthy == None or d < closestDistance) :
                        Healthy = u2.getMaxHitPoints()
                        closestHealthy = u2
                        closestDistance =d
	                
        return closestHealthy
    
    
    def getUnitWeakest(self,gs : GameState, p : Player, u : Unit) -> Unit:
        pgs = gs.getPhysicalGameState()
        closestWeakest = None
        closestDistance = 0
        Weakest = 10000
        
        
        for  u2 in pgs.getUnits(): 
            if u2.getPlayer() >= 0 and u2.getPlayer() != p.getID() and u.getID() != u2.getID():
                d = abs(u2.getX() - u.getX()) + abs(u2.getY() - u.getY())
                if closestWeakest == None or Weakest > u2.getMaxDamage():
                    Weakest = u2.getMaxDamage()
                    closestWeakest = u2
                    closestDistance =d
                elif Weakest == u2.getMaxDamage():
                    if closestWeakest == None or d < closestDistance:
                        closestWeakest = u2
                        closestDistance = d
                        Weakest = u2.getMaxDamage()
	      
        return closestWeakest
	
    
    def behaveBase(self,u:Unit, player:int,  gs:GameState):
        nW=self.countUnit("Worker",player,gs)
        if nW < 2 and self.resource >=self.workerType.cost:
            self._core.train(u,self.workerType)
        
    def behaveWr(self,u:Unit, player:int,  gs:GameState):
        
        nBr = self.countConstrution("Barracks",player,gs)
        p = gs.getPlayer(player)
        reservedPositions = java.util.LinkedList()
        pgs = gs.getPhysicalGameState()
        
        if self._core.getAbstractAction(u)==None and nBr <1:
            r = self._core.buildIfNotAlreadyBuilding(u,self.barracksType,u.getX(),u.getY(),reservedPositions,p,pgs)
            
        
   '''