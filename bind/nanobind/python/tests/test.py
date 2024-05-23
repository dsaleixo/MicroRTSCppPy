import sys
print(sys.version)
from MicroRTS_NB import PhysicalGameState
from MicroRTS_NB  import  UnitTypeTable
from MicroRTS_NB  import Unit
 


if __name__ == '__main__':
    utt = UnitTypeTable(2);
    #print(utt.VERSION_NON_DETERMINISTIC)
    psg = PhysicalGameState.load("../maps/basesWorkers32x32A.xml",utt);

    print("Units0")
    for u in psg.getUnits(0).values():
        print (u.toString());
    print("Units1")
    for u in psg.getUnits(1).values():
        print (u.toString());
    print("UnitsR")
    for u in psg.getUnits(-1).values():
        print (u.toString());
    