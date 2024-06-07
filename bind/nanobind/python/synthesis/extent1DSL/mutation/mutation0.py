

from synthesis.baseDSL.mainBase.node import Node
from synthesis.extent1DSL.mutation.mutation import Mutation

from synthesis.extent1DSL.util.Factory_E1 import Factory_E1
import random

class Mutation0(Mutation):
    
    def __init__(self):
        self._f = Factory_E1()
    
    
    def getMutations(self, prog, n_mutation) -> list[Node]:
        l_progs = []
        for _ in range(n_mutation):
            mutation = prog.clone(self._f)
            l= []
            mutation.countNode(l)
            no = l[random.randint(0, len(l)-1)]
            no.mutation(15)
            l_progs.append(mutation)
        return l_progs