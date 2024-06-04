import sys


from playout.tests.test0 import Test0
from synthesis.baseDSL.tests.scriptsTests import ScriptsTests
from synthesis.extent1DSL.tests.sampleMutation import SampleMutation

if __name__ == "__main__":
    map = "./maps/basesWorkers32x32A.xml"
    SampleMutation.test2()
    