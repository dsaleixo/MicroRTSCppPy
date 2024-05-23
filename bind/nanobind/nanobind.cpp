#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/unordered_map.h>
#include <nanobind/stl/unordered_set.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/pair.h>
#include "UnitTypeTable.h"
#include "PhysicalGameState.h"
#include "Unit.h"
#include "UnitType.h"
#include "AStarPathFinding.h"
#include "GameState.h"
#include "PlayerAction.h"
#include "ResourceUsage.h"
#include "UnitAction.h"
#include "UnitActionAssignment.h"


#include <stdio.h>

int add(int a, int b) { return a + b; }


namespace nb = nanobind;
NB_MODULE(MicroRTS_NB, m) {
	m.def("add", &add);

	nb::class_<UnitTypeTable>(m, "UnitTypeTable")
		.def(nb::init<>())
        	.def(nb::init<int>())
        	.def(nb::init<int, int>())
        	.def("setUnitTypeTable", &UnitTypeTable::setUnitTypeTable)
        	.def("addUnitType", &UnitTypeTable::addUnitType)
        	.def("getUnitTypeString", &UnitTypeTable::getUnitTypeString, nb::rv_policy::reference)
       		.def("getUnitTypes", &UnitTypeTable::getUnitTypes, nb::rv_policy::reference)
       		.def("getMoveConflictResolutionStrategy", &UnitTypeTable::getMoveConflictResolutionStrategy)
        	.def("getUnit", &UnitTypeTable::getUnitTypes);



	 nb::class_<UnitType>(m, "UnitType")
        .def("equals", &UnitType::equals)
        .def("getName", &UnitType::getName)
        .def("getIsStockpile", &UnitType::getIsStockpile)
        .def("getCanMove", &UnitType::getCanMove)
        .def("getCanAttack", &UnitType::getCanAttack)
        .def("getcanHarvest", &UnitType::getcanHarvest)
        .def("getisResource", &UnitType::getisResource)
        .def("produces", &UnitType::produces);

	nb::class_<Player>(m, "Player")
        .def(nb::init<int, int>())
        .def("getID", &Player::getID)
        .def("getResources", &Player::getResources)
        .def("setResources", &Player::setResources)
        .def("toString", &Player::toString)
        .def("fromXML", &Player::fromXML)
        .def("clone", &Player::clone);

	nb::class_<Unit>(m, "Unit")
        	.def(nb::init<long, int, UnitType*, int, int, int>())
        	.def(nb::init<int, UnitType*, int, int, int>())
        	.def(nb::init<int, UnitType*, int, int>())
        	.def(nb::init<const Unit>())
         
        	.def("getPlayer", &Unit::getPlayer)
        	.def("getType", &Unit::getType, nb::rv_policy::reference)
        	.def("setType", &Unit::setType)
        	.def("getID", &Unit::getID)
       		.def("getX", &Unit::getX)
        	.def("getY", &Unit::getY)
        	.def("setX", &Unit::setX)
        	.def("setY", &Unit::setY)
        	.def("getResources", &Unit::getResources)
        	.def("getAttackRange", &Unit::getAttackRange)
        	.def("setResources", &Unit::setResources)
        	.def("getHitPoints", &Unit::getHitPoints)
        	.def("getMaxHitPoints", &Unit::getMaxHitPoints)
        	.def("setHitPoints", &Unit::setHitPoints)
       		.def("getCost", &Unit::getCost)
       		.def("getMoveTime", &Unit::getMoveTime)
       		.def("getAttackTime", &Unit::getAttackTime)
       		.def("getMinDamage", &Unit::getMinDamage)
       		.def("getMaxDamage", &Unit::getMaxDamage)
        	.def("getHarvestAmount", &Unit::getHarvestAmount)
        	.def("getHarvestTime", &Unit::getHarvestTime)
        	.def("toString", &Unit::toString)
        
        	.def("hashCode", &Unit::hashCode)
        	.def("getUnitActions", &Unit::getUnitActions, nb::rv_policy::reference)
        	.def("setID", &Unit::setID);


		nb::class_<PhysicalGameState>(m, "PhysicalGameState")
        .def(nb::init<int,int>())
        .def("load", &PhysicalGameState::load)
   
        .def("getUnits", &PhysicalGameState::getUnits, nb::rv_policy::reference)
        .def("addUnit", &PhysicalGameState::addUnit)
        .def("addPlayer", &PhysicalGameState::addPlayer)
        .def("getPlayer", &PhysicalGameState::getPlayer)
        .def("getWidth", &PhysicalGameState::getWidth)
        .def("getHeight", &PhysicalGameState::getHeight)
        .def("getTerrain", &PhysicalGameState::getTerrain)
        .def("getTERRAIN_WALL", &PhysicalGameState::getTERRAIN_WALL)
        .def("winner", &PhysicalGameState::winner)
        .def("gameover", &PhysicalGameState::gameover)
	.def("getUnitAt", &PhysicalGameState::getUnitAt,nb::rv_policy::reference)
        .def("getUnit", &PhysicalGameState::getUnit,nb::rv_policy::reference);


	 nb::class_<AStarPathFinding>(m, "AStarPathFinding")
        .def(nb::init<int,int>())
        .def("findPathToAdjacentPosition", &AStarPathFinding::findPathToAdjacentPosition)
        .def("findPathToPositionInRange", &AStarPathFinding::findPathToPositionInRange);

 nb::class_<UnitActionAssignment>(m, "UnitActionAssignment")
        .def("getIdUnit", &UnitActionAssignment::getIdUnit)
        .def("getUnitAction", &UnitActionAssignment::getUnitAction)
        .def("getTime", &UnitActionAssignment::getTime)
        .def("toString", &UnitActionAssignment::toString);

    nb::class_<UnitAction>(m, "UnitAction")
        .def(nb::init<int>())
        .def(nb::init<int, int>())
        .def(nb::init<int, int, int>())
        .def(nb::init<int, int, UnitType*>())
        .def("toString", &UnitAction::toString)
        .def("resourceUsage", &UnitAction::resourceUsage)
        .def("getDirection", &UnitAction::getDirection)
        .def("getLocationX", &UnitAction::getLocationX)
        .def("getLocationY", &UnitAction::getLocationY)
        .def("getType", &UnitAction::getType)
        .def("ETA", &UnitAction::ETA)
        .def("getActionName", &UnitAction::getActionName)
        .def("getTYPE_NONE", &UnitAction::getTYPE_NONE)
        .def("getTYPE_MOVE", &UnitAction::getTYPE_MOVE)
        .def("getTYPE_HARVEST", &UnitAction::getTYPE_HARVEST)
        .def("getTYPE_RETURN", &UnitAction::getTYPE_RETURN)
        .def("getTYPE_PRODUCE", &UnitAction::getTYPE_PRODUCE)
        .def("getTYPE_ATTACK_LOCATION", &UnitAction::getTYPE_ATTACK_LOCATION)
        .def("getNUMBER_OF_ACTION_TYPES", &UnitAction::getNUMBER_OF_ACTION_TYPES)
        .def("getDIRECTION_NONE", &UnitAction::getDIRECTION_NONE)
        .def("getDIRECTION_UP", &UnitAction::getDIRECTION_UP)
        .def("getDIRECTION_RIGHT", &UnitAction::getDIRECTION_RIGHT)
        .def("getDIRECTION_DOWN", &UnitAction::getDIRECTION_DOWN)
        .def("getDIRECTION_LEFT", &UnitAction::getDIRECTION_LEFT);

    nb::class_<PlayerAction>(m, "PlayerAction")
        .def(nb::init<>())
        .def("fillWithNones", &PlayerAction::fillWithNones)
        .def("getResourceUsage", &PlayerAction::getResourceUsage, nb::rv_policy::reference)
        .def("setResourceUsage", &PlayerAction::setResourceUsage)
        .def("consistentWith", &PlayerAction::consistentWith)
        .def("getActions", &PlayerAction::getActions, nb::rv_policy::reference)
        .def("addUnitAction", &PlayerAction::addUnitAction);

nb::class_<GameState>(m, "GameState")
        .def(nb::init<PhysicalGameState*, UnitTypeTable*>())
        .def(nb::init<GameState&>())
        .def("getActionAssignment", &GameState::getActionAssignment, nb::rv_policy::reference)
        .def("getTime", &GameState::getTime)
        .def("free", &GameState::free)
        .def("getNextChangeTime", &GameState::getNextChangeTime)
        .def("isUnitActionAllowed", &GameState::isUnitActionAllowed)
        .def("issueSafe", &GameState::issueSafe)
        .def("getPlayer", &GameState::getPlayer)
        .def("cycle", &GameState::cycle)
        .def("getResourceUsage", &GameState::getResourceUsage)
        .def("winner", &GameState::winner)
        .def("gameover", &GameState::gameover)
        .def("updateScream", &GameState::updateScream)
        .def("getPhysicalGameState", &GameState::getPhysicalGameState, nb::rv_policy::reference);

	nb::class_<ResourceUsage>(m, "ResourceUsage")
        .def(nb::init<>())
        .def("merge", &ResourceUsage::merge)
        .def("getPositionsUsed", &ResourceUsage::getPositionsUsed)
        .def("toString", &ResourceUsage::toString)
        .def("consistentWith", &ResourceUsage::consistentWith);

}

/*


*/

