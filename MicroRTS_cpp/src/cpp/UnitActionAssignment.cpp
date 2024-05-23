#include "UnitActionAssignment.h"
#include "UnitAction.h"
#include "Unit.h"
#include <iostream>

Unit& UnitActionAssignment::getUnit() {
    return this->unit;
}
int UnitActionAssignment::getIdUnit() {
    return this->unit.getID();
}
UnitAction& UnitActionAssignment::getUnitAction() {
    return this->action;
}
int UnitActionAssignment::getTime() {
    return this->time;
}



UnitActionAssignment::~UnitActionAssignment() {
	
    
}
UnitActionAssignment::UnitActionAssignment(Unit &a_unit, UnitAction &a_action, int a_time) {
    this->unit = a_unit;
    this->action = a_action;
    //if (action == nullptr) {
    //std::cout << "UnitActionAssignment with null action! "<< this->action.r_cache << endl;
    //}
    this->time = a_time;

}

string UnitActionAssignment::toString() {
    return "uaa : {"+to_string(this->time)+", " + this->unit.toString() + ", " + this->action.toString() + "}";
}