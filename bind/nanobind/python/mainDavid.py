import sys


from playout.tests.test0 import Test0
from synthesis.baseDSL.tests.scriptsTests import ScriptsTests

if __name__ == "__main__":
    map = "./maps/basesWorkers32x32A.xml"
    ScriptsTests.test0()
    