#include "PlayerAction.h"
#include "GameState.h"
unordered_map< int, pair<Unit, UnitAction>>& PlayerAction::getActions() {
	return this->actions;
}

void PlayerAction::setResourceUsage(ResourceUsage& a_r) {
	delete this->r;
	
	this->r = new ResourceUsage(a_r);
}


bool PlayerAction::consistentWith(ResourceUsage &u, GameState* gs) {
	return this->r->consistentWith(u, gs);
}

void PlayerAction::fillWithNones(GameState* s, int pID, int duration) {
	PhysicalGameState *pgs = s->getPhysicalGameState();
	for (auto& aux : pgs->getUnits(pID)) {
		Unit *u = aux.second;
		
		if (s->unitActions.find(u->ID) == s->unitActions.end()) {
			bool found = this->actions.find(u->ID) == this->actions.end();
			
			if (found) {
				actions.insert({ u->ID,make_pair<>(*u, UnitAction(UnitAction::TYPE_NONE, duration)) });
			}
		}
		
	}
}

ResourceUsage* PlayerAction::getResourceUsage() {
	return this->r;
}

void PlayerAction::addUnitAction(Unit &u, UnitAction &a) {
	this->actions.insert({ u.ID,make_pair<>(u, a) });
}


bool PlayerAction::integrityCheck() {
	int player = -1;
	
	for (auto& aux : actions) {
		auto& uaa = aux.second;
		Unit& u = uaa.first;
		if (player == -1) {
			player = u.getPlayer();
		}
		else {
			if (player != u.getPlayer()) {
				cout << "integrityCheck: units from more than one player!" << endl;
				return false;
			}
		}
	}
	return true;
}

PlayerAction::PlayerAction(){
	this->r = new ResourceUsage();
}

PlayerAction::~PlayerAction() {
	this->actions.clear();
	delete this->r;
}