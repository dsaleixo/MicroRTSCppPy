
import jpype 
import jpype.imports
from jpype import * 



jpype.startJVM(jpype.getDefaultJVMPath(), classpath= ['jars/*'])

class GameStateJavaPy:
    def __init__(self,map):
        self._map = map
        