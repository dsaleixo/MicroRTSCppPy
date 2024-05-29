#include "PhysicalGameState.h"
#include "Player.h"
#include "Unit.h"
#include "pugixml.hpp"
#include "unordered_map"


using namespace  std;


PhysicalGameState::PhysicalGameState(const PhysicalGameState& other) {
    Unit::next_ID = 1237;
    
    this->width = other.width;
    this->height = other.height;
    for (auto it : other.terrain)this->terrain.push_back(it);
    for (const auto &p : other.players) {
        
        this->players.push_back(Player(p.getID(), p.getResources()));
    }
    for (auto &aux : other.unitsP0) {
        Unit* u = new Unit(*(aux.second));
         this->addUnit(*u);
    }for (auto& aux : other.unitsP1) {
        Unit* u = new Unit(*(aux.second));
        this->addUnit(*u);
    }for (auto& aux : other.unitsR) {
        Unit* u = new Unit(*(aux.second));
        this->addUnit(*u);
    }
  
}


bool** PhysicalGameState::getAllFree() {
    bool **free = new bool* [this->getWidth()];
    for (int i = 0; i < this->getWidth(); i++) free[i] = new bool[this->getHeight()];


    for (int x = 0; x < getWidth(); x++) {
        for (int y = 0; y < getHeight(); y++) {
            free[x][y] = getTerrain(x, y) == PhysicalGameState::TERRAIN_NONE;
        }
    }
    for (auto& aux : this->unitsP0) {
        Unit *u = aux.second;
        free[u->getX()][u->getY()] = false;
    }
    for (auto& aux : this->unitsP1) {
        Unit* u = aux.second;
        free[u->getX()][u->getY()] = false;
    }
    for (auto& aux : this->unitsR) {
        Unit* u = aux.second;
        free[u->getX()][u->getY()] = false;
    }

    return free;
}


int PhysicalGameState::winner() {
    
    int unitcounts[] = { 0,0 };
    int totalunits = 0;
    for (auto& aux : this->unitsP0) {
        Unit *u = aux.second;
        unitcounts[0]++;
    }
    for (auto& aux : this->unitsP1) {
        Unit* u = aux.second;
        unitcounts[1]++;
    }
    int winner = -1;
    for (int i = 0; i < 2; i++) {
        if (unitcounts[i] > 0) {
            if (winner == -1) {
                winner = i;
            }
            else {
                return -1;
            }
        }
    }

    return winner;
}

bool PhysicalGameState::gameover() {
    int unitcounts[] = {0,0};
    int totalunits = 0;
  
    for (auto &aux : this->unitsP0) {
        Unit *u = aux.second; 
      
        unitcounts[0]++;
        totalunits++;
    }
  
    for (auto& aux : this->unitsP1) {
        Unit* u = aux.second;
      
        unitcounts[1]++;
        totalunits++;
    }
   
    if (totalunits == 0) {
        return true;
    }

    int winner = -1;
    for (int i = 0; i < 2; i++) {
        if (unitcounts[i] > 0) {
            if (winner == -1) {
                winner = i;
            }
            else {
                return false;
            }
        }
    }

    return winner != -1;
}

void PhysicalGameState::removeUnit(Unit &u) {
    if (u.getPlayer() == 0) {
     
        auto f = this->unitsP0.find(u.ID);
        if (f != this->unitsP0.end()) {
            delete f->second;
            this->unitsP0.erase(u.ID);
        }
    }
    else if (u.getPlayer() == 1) {
        auto f = this->unitsP1.find(u.ID);
        if (f != this->unitsP1.end()) {
            delete f->second;
            this->unitsP1.erase(u.ID);
        }
    }
    else  {
            auto f = this->unitsP0.find(u.ID);
            if (f != this->unitsP0.end()) {
                delete f->second;
                this->unitsP0.erase(u.ID);
            }
    }
    
}

Unit* PhysicalGameState::getUnitAt(int x, int y) {
    for ( auto &u : this->unitsP0) {
        if (u.second->getX() == x && u.second->getY() == y) {
            return u.second;
        }
    }
    for (auto& u : this->unitsP1) {
        if (u.second->getX() == x && u.second->getY() == y) {
            return u.second;
        }
    }
    for (auto& u : this->unitsR) {
        if (u.second->getX() == x && u.second->getY() == y) {
            return u.second;
        }
    }
    
    return nullptr;
}

Player& PhysicalGameState::getPlayer(int pID) {
    return this->players[pID];
}

int PhysicalGameState::getWidth() {
    return this->width;
}


int PhysicalGameState::getHeight() {
    return this->height;
}


int PhysicalGameState::getTERRAIN_WALL() {
    return TERRAIN_WALL;
}

/**
         * Returns what is on a given position of the terrain
         *
         * @param x
         * @param y
         * @return
         */
int PhysicalGameState::getTerrain(int x, int y) {

    return this->terrain[x + y * this->width];

}


PhysicalGameState::PhysicalGameState(int a_width, int a_height) {
    this->width = a_width;
    this->height = a_height;
    
}

PhysicalGameState::PhysicalGameState(int a_width, int a_height, vector<int> &a_terrain) {
    this->width = a_width;
    this->height = a_height;
    this->terrain = a_terrain;

}


PhysicalGameState::~PhysicalGameState() {
    
    this->terrain.clear();
    this->players.clear();

    for (auto it = unitsP0.begin(); it != unitsP0.end(); ++it)
    {
        delete it->second;
        it->second = nullptr;
        unitsP0.erase(it->first);
    }
    for (auto it = unitsP1.begin(); it != unitsP1.end(); ++it)
    {
        delete it->second;
        it->second = nullptr;
        unitsP1.erase(it->first);
    }
    for (auto it = unitsR.begin(); it != unitsR.end(); ++it)
    {
        delete it->second;
        it->second = nullptr;
        unitsR.erase(it->first);
    }
    
    
}

Unit* PhysicalGameState::getUnit(int ID,int player) {
    if (player == 0) {
        auto aux = this->unitsP0.find(ID);
        if (aux != this->unitsP0.end())return aux->second;
    } else if (player == 1) {
        auto aux = this->unitsP1.find(ID);
        if (aux != this->unitsP1.end())return aux->second;
    }else if (player == -1) {
        auto aux = this->unitsR.find(ID);
        if (aux != this->unitsR.end())return aux->second;
    }
    
    return nullptr;
}


vector<int> PhysicalGameState::getTerrainFromUnknownString(string terrainString, int size) {
    vector<int> terrain;
   //if (terrainString.contains("A") || terrainString.contains("B")) {
   //     terrain = uncompressTerrain(terrainString);
   // }
    //else {
    
        for (int i = 0; i < size; i++) {
            
            terrain.push_back( (int) terrainString[i]-48);
            
        }
       
    //}

    return terrain;
}


PhysicalGameState* PhysicalGameState::fromXML(pugi::xml_node &e, UnitTypeTable &utt) {
    pugi::xml_node terrain_e = e.child("terrain");
    pugi::xml_node players_e = e.child("players");
    pugi::xml_node units_e = e.child("units");

    int width = e.attribute("width").as_int();
    int height = e.attribute("height").as_int();
   
    
    string ss = terrain_e.child_value();
   
    vector<int> terrain = getTerrainFromUnknownString(ss, width * height);
    
    PhysicalGameState *pgs = new  PhysicalGameState(width, height,terrain);
    
    for (pugi::xml_node o : players_e.children()) {
        Player p = Player::fromXML(o);
       
        pgs->addPlayer(p);
    }
    
    
    for (pugi::xml_node o : units_e.children()) {
       
        Unit u = Unit::fromXML(o, utt);
        // check for repeated IDs:
        if (pgs->getUnit(u.getID(),u.getPlayer()) != nullptr) {
            cout << "error pgs fromXML" << endl;
        }
      
        pgs->addUnit(u);
    }
    
    return pgs;
}

void PhysicalGameState::addPlayer(Player &p) {
    this->players.push_back(p);
}

unordered_map< int, Unit*>& PhysicalGameState::getUnits(int player) {
    if (player==0)return this->unitsP0;
    if (player == 1)return this->unitsP1;
    if (player == -1)return this->unitsR;

}

/**
     * Adds a new {@link Unit} to the map if its position is free
     *
     * @param newUnit
     * @throws IllegalArgumentException if the new unit's position is already
     * occupied
     */
    void PhysicalGameState::addUnit(Unit &newUnit) {
    /*
    for (Unit existingUnit : units) {
        if (newUnit.getX() == existingUnit.getX() && newUnit.getY() == existingUnit.getY()) {
            throw new IllegalArgumentException(
                "PhysicalGameState.addUnit: added two units in position: (" + newUnit.getX() + ", " + newUnit.getY() + ")");
        }
    }
    */
        if(newUnit.getPlayer() == 0)this->unitsP0.insert({newUnit.ID,new Unit(newUnit)});
        else if (newUnit.getPlayer() == 1)this->unitsP1.insert({ newUnit.ID,new Unit(newUnit) });
        else if (newUnit.getPlayer() == -1)this->unitsR.insert({ newUnit.ID,new Unit(newUnit) });
}


PhysicalGameState*  PhysicalGameState::load(string fileName, UnitTypeTable &utt) {
     
	 pugi::xml_document doc;
	 pugi::xml_parse_result result = doc.load_file(fileName.c_str());
	 if (!result) {
		 cout<<"Error: Read map"<< fileName<<endl;
     }
     else {
         
         for (pugi::xml_node n : doc.children()) {
             cout << n.name() << endl;
         }
         auto aux =doc.child("rts.PhysicalGameState");
         return PhysicalGameState::fromXML(aux, utt);

     }


}
