from typing import Any, Optional, overload, Typing, Sequence, Iterable, Union, Callable
from enum import Enum
import MicroRTS_NB.MicroRTS_NB

class AStarPathFinding:
    """
    None
    """

    def __init__(self, arg0: int, arg1: int, /) -> None:
        ...
    
    def findPathToAdjacentPosition(self, arg0: MicroRTS_NB.MicroRTS_NB.Unit, arg1: int, arg2: MicroRTS_NB.MicroRTS_NB.GameState, /) -> MicroRTS_NB.MicroRTS_NB.UnitAction:
        ...
    
    def findPathToPositionInRange(self, arg0: MicroRTS_NB.MicroRTS_NB.Unit, arg1: int, arg2: int, arg3: MicroRTS_NB.MicroRTS_NB.GameState, /) -> MicroRTS_NB.MicroRTS_NB.UnitAction:
        ...
    
class GameState:
    """
    None
    """

    def __init__(self, arg: MicroRTS_NB.MicroRTS_NB.GameState) -> None:
        """
        __init__(self, arg: MicroRTS_NB.MicroRTS_NB.GameState) -> None
        """
        ...
    
    @overload
    def __init__(self, arg0: MicroRTS_NB.MicroRTS_NB.PhysicalGameState, arg1: MicroRTS_NB.MicroRTS_NB.UnitTypeTable, /) -> None:
        """
        __init__(self, arg0: MicroRTS_NB.MicroRTS_NB.PhysicalGameState, arg1: MicroRTS_NB.MicroRTS_NB.UnitTypeTable, /) -> None
        """
        ...
    
    def cycle(self) -> bool:
        ...
    
    def free(self, arg0: int, arg1: int, /) -> bool:
        ...
    
    def gameover(self) -> bool:
        ...
    
    def getActionAssignment(self, arg: MicroRTS_NB.MicroRTS_NB.Unit, /) -> MicroRTS_NB.MicroRTS_NB.UnitActionAssignment:
        ...
    
    def getNextChangeTime(self) -> int:
        ...
    
    def getPhysicalGameState(self) -> MicroRTS_NB.MicroRTS_NB.PhysicalGameState:
        ...
    
    def getPlayer(self, arg: int, /) -> MicroRTS_NB.MicroRTS_NB.Player:
        ...
    
    def getResourceUsage(self) -> MicroRTS_NB.MicroRTS_NB.ResourceUsage:
        ...
    
    def getTime(self) -> int:
        ...
    
    def isUnitActionAllowed(self, arg0: MicroRTS_NB.MicroRTS_NB.Unit, arg1: MicroRTS_NB.MicroRTS_NB.UnitAction, /) -> bool:
        ...
    
    def issueSafe(self, arg: MicroRTS_NB.MicroRTS_NB.PlayerAction, /) -> bool:
        ...
    
    def updateScream(self) -> bool:
        ...
    
    def winner(self) -> int:
        ...
    
class PhysicalGameState:
    """
    None
    """

    def __init__(self, arg0: int, arg1: int, /) -> None:
        ...
    
    def addPlayer(self, arg: MicroRTS_NB.MicroRTS_NB.Player, /) -> None:
        ...
    
    def addUnit(self, arg: MicroRTS_NB.MicroRTS_NB.Unit, /) -> None:
        ...
    
    def gameover(self) -> bool:
        ...
    
    def getHeight(self) -> int:
        ...
    
    def getPlayer(self, arg: int, /) -> MicroRTS_NB.MicroRTS_NB.Player:
        ...
    
    def getTERRAIN_WALL() -> int:
        ...
    
    def getTerrain(self, arg0: int, arg1: int, /) -> int:
        ...
    
    def getUnit(self, arg0: int, arg1: int, /) -> MicroRTS_NB.MicroRTS_NB.Unit:
        ...
    
    def getUnitAt(self, arg0: int, arg1: int, /) -> MicroRTS_NB.MicroRTS_NB.Unit:
        ...
    
    def getUnits(self, arg: int, /) -> dict[int, MicroRTS_NB.MicroRTS_NB.Unit]:
        ...
    
    def getWidth(self) -> int:
        ...
    
    def load(self, arg: MicroRTS_NB.MicroRTS_NB.UnitTypeTable, /) -> MicroRTS_NB.MicroRTS_NB.PhysicalGameState:
        ...
    
    def winner(self) -> int:
        ...
    
class Player:
    """
    None
    """

    def __init__(self, arg0: int, arg1: int, /) -> None:
        ...
    
    def clone(self) -> MicroRTS_NB.MicroRTS_NB.Player:
        ...
    
    def fromXML(self) -> MicroRTS_NB.MicroRTS_NB.Player:
        ...
    
    def getID(self) -> int:
        ...
    
    def getResources(self) -> int:
        ...
    
    def setResources(self, arg: int, /) -> None:
        ...
    
    def toString(self) -> str:
        ...
    
class PlayerAction:
    """
    None
    """

    def __init__(self) -> None:
        ...
    
    def addUnitAction(self, arg0: MicroRTS_NB.MicroRTS_NB.Unit, arg1: MicroRTS_NB.MicroRTS_NB.UnitAction, /) -> None:
        ...
    
    def consistentWith(self, arg0: MicroRTS_NB.MicroRTS_NB.ResourceUsage, arg1: MicroRTS_NB.MicroRTS_NB.GameState, /) -> bool:
        ...
    
    def fillWithNones(self, arg0: MicroRTS_NB.MicroRTS_NB.GameState, arg1: int, arg2: int, /) -> None:
        ...
    
    def getActions(self) -> dict[int, tuple[MicroRTS_NB.MicroRTS_NB.Unit, MicroRTS_NB.MicroRTS_NB.UnitAction]]:
        ...
    
    def getResourceUsage(self) -> MicroRTS_NB.MicroRTS_NB.ResourceUsage:
        ...
    
    def setResourceUsage(self, arg: MicroRTS_NB.MicroRTS_NB.ResourceUsage, /) -> None:
        ...
    
class ResourceUsage:
    """
    None
    """

    def __init__(self) -> None:
        ...
    
    def consistentWith(self, arg0: MicroRTS_NB.MicroRTS_NB.ResourceUsage, arg1: MicroRTS_NB.MicroRTS_NB.GameState, /) -> bool:
        ...
    
    def getPositionsUsed(self) -> list[int]:
        ...
    
    def merge(self, arg: MicroRTS_NB.MicroRTS_NB.ResourceUsage, /) -> None:
        ...
    
    def toString(self) -> str:
        ...
    
class Unit:
    """
    None
    """

    def __init__(self, arg: MicroRTS_NB.MicroRTS_NB.Unit) -> None:
        """
        __init__(self, arg: MicroRTS_NB.MicroRTS_NB.Unit) -> None
        """
        ...
    
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: MicroRTS_NB.MicroRTS_NB.UnitType, arg3: int, arg4: int, arg5: int, /) -> None:
        """
        __init__(self, arg0: int, arg1: int, arg2: MicroRTS_NB.MicroRTS_NB.UnitType, arg3: int, arg4: int, arg5: int, /) -> None
        """
        ...
    
    @overload
    def __init__(self, arg0: int, arg1: MicroRTS_NB.MicroRTS_NB.UnitType, arg2: int, arg3: int, arg4: int, /) -> None:
        """
        __init__(self, arg0: int, arg1: MicroRTS_NB.MicroRTS_NB.UnitType, arg2: int, arg3: int, arg4: int, /) -> None
        """
        ...
    
    @overload
    def __init__(self, arg0: int, arg1: MicroRTS_NB.MicroRTS_NB.UnitType, arg2: int, arg3: int, /) -> None:
        """
        __init__(self, arg0: int, arg1: MicroRTS_NB.MicroRTS_NB.UnitType, arg2: int, arg3: int, /) -> None
        """
        ...
    
    def clone(self) -> MicroRTS_NB.MicroRTS_NB.Unit:
        ...
    
    def getAttackRange(self) -> int:
        ...
    
    def getAttackTime(self) -> int:
        ...
    
    def getCost(self) -> int:
        ...
    
    def getHarvestAmount(self) -> int:
        ...
    
    def getHarvestTime(self) -> int:
        ...
    
    def getHitPoints(self) -> int:
        ...
    
    def getID(self) -> int:
        ...
    
    def getMaxDamage(self) -> int:
        ...
    
    def getMaxHitPoints(self) -> int:
        ...
    
    def getMinDamage(self) -> int:
        ...
    
    def getMoveTime(self) -> int:
        ...
    
    def getNextID0()(*args, **kwargs):
        """
        getNextID0()(self) -> int
        """
        ...
    
    def getPlayer(self) -> int:
        ...
    
    def getResources(self) -> int:
        ...
    
    def getType(self) -> MicroRTS_NB.MicroRTS_NB.UnitType:
        ...
    
    def getUnitActions(self, arg: MicroRTS_NB.MicroRTS_NB.GameState, /) -> list[MicroRTS_NB.MicroRTS_NB.UnitAction]:
        ...
    
    def getX(self) -> int:
        ...
    
    def getY(self) -> int:
        ...
    
    def hashCode(self) -> int:
        ...
    
    def setHitPoints(self, arg: int, /) -> None:
        ...
    
    def setID(self, arg: int, /) -> None:
        ...
    
    def setNextID0()(*args, **kwargs):
        """
        setNextID0()(self, arg: int, /) -> None
        """
        ...
    
    def setResources(self, arg: int, /) -> None:
        ...
    
    def setType(self, arg: MicroRTS_NB.MicroRTS_NB.UnitType, /) -> None:
        ...
    
    def setX(self, arg: int, /) -> None:
        ...
    
    def setY(self, arg: int, /) -> None:
        ...
    
    def toString(self) -> str:
        ...
    
class UnitAction:
    """
    None
    """

    def ETA(self, arg: MicroRTS_NB.MicroRTS_NB.Unit, /) -> int:
        ...
    
    def __init__(self, arg0: int, arg1: int, arg2: MicroRTS_NB.MicroRTS_NB.UnitType, /) -> None:
        """
        __init__(self, arg0: int, arg1: int, arg2: MicroRTS_NB.MicroRTS_NB.UnitType, /) -> None
        """
        ...
    
    @overload
    def __init__(self, arg: int, /) -> None:
        """
        __init__(self, arg: int, /) -> None
        """
        ...
    
    @overload
    def __init__(self, arg0: int, arg1: int, /) -> None:
        """
        __init__(self, arg0: int, arg1: int, /) -> None
        """
        ...
    
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, /) -> None:
        """
        __init__(self, arg0: int, arg1: int, arg2: int, /) -> None
        """
        ...
    
    def getActionName(self) -> str:
        ...
    
    def getDIRECTION_DOWN() -> int:
        ...
    
    def getDIRECTION_LEFT() -> int:
        ...
    
    def getDIRECTION_NONE() -> int:
        ...
    
    def getDIRECTION_RIGHT() -> int:
        ...
    
    def getDIRECTION_UP() -> int:
        ...
    
    def getDirection(self) -> int:
        ...
    
    def getLocationX(self) -> int:
        ...
    
    def getLocationY(self) -> int:
        ...
    
    def getNUMBER_OF_ACTION_TYPES() -> int:
        ...
    
    def getTYPE_ATTACK_LOCATION() -> int:
        ...
    
    def getTYPE_HARVEST() -> int:
        ...
    
    def getTYPE_MOVE() -> int:
        ...
    
    def getTYPE_NONE() -> int:
        ...
    
    def getTYPE_PRODUCE() -> int:
        ...
    
    def getTYPE_RETURN() -> int:
        ...
    
    def getType(self) -> int:
        ...
    
    def resourceUsage(self, arg0: MicroRTS_NB.MicroRTS_NB.Unit, arg1: MicroRTS_NB.MicroRTS_NB.PhysicalGameState, /) -> MicroRTS_NB.MicroRTS_NB.ResourceUsage:
        ...
    
    def toString(self) -> str:
        ...
    
class UnitActionAssignment:
    """
    None
    """

    def __init__(*args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
    
    def getIdUnit(self) -> int:
        ...
    
    def getTime(self) -> int:
        ...
    
    def getUnitAction(self) -> MicroRTS_NB.MicroRTS_NB.UnitAction:
        ...
    
    def toString(self) -> str:
        ...
    
class UnitType:
    """
    None
    """

    def __init__(*args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
    
    def equals(self, arg: MicroRTS_NB.MicroRTS_NB.UnitType, /) -> bool:
        ...
    
    def getCanAttack(self) -> bool:
        ...
    
    def getCanMove(self) -> bool:
        ...
    
    def getIsStockpile(self) -> bool:
        ...
    
    def getName(self) -> str:
        ...
    
    def getcanHarvest(self) -> bool:
        ...
    
    def getisResource(self) -> bool:
        ...
    
    def produces(self, arg: MicroRTS_NB.MicroRTS_NB.UnitType, /) -> None:
        ...
    
class UnitTypeTable:
    """
    None
    """

    def __init__(self, arg0: int, arg1: int, /) -> None:
        """
        __init__(self, arg0: int, arg1: int, /) -> None
        """
        ...
    
    @overload
    def __init__(self) -> None:
        """
        __init__(self) -> None
        """
        ...
    
    @overload
    def __init__(self, arg: int, /) -> None:
        """
        __init__(self, arg: int, /) -> None
        """
        ...
    
    def addUnitType(self, arg: MicroRTS_NB.MicroRTS_NB.UnitType, /) -> None:
        ...
    
    def getMoveConflictResolutionStrategy(self) -> int:
        ...
    
    def getUnit(self) -> list[MicroRTS_NB.MicroRTS_NB.UnitType]:
        ...
    
    def getUnitTypeString(self, arg: str, /) -> MicroRTS_NB.MicroRTS_NB.UnitType:
        ...
    
    def getUnitTypes(self) -> list[MicroRTS_NB.MicroRTS_NB.UnitType]:
        ...
    
    def setUnitTypeTable(self, arg0: int, arg1: int, /) -> None:
        ...
    
def add(arg0: int, arg1: int, /) -> int:
    ...

