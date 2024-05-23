import sys
from tests.test6 import Test6


if __name__ == "__main__":
    
    #map = "./maps/mapadavid2.xml"
    #map = "./maps/basesWorkers32x32A.xml"
    #map = "./maps/(4)BloodBath.scmB.xml"
    map = "./maps/map0.xml"
    test = Test6()
    arg = sys.argv[1]
    print("arg",arg)
    print()
    test.test(map,arg)