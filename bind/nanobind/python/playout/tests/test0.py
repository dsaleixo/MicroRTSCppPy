

from MicroRTS_NB import GameState, PhysicalGameState, UnitTypeTable

from ai.rush.CombatRush import CombatRush
from playout.simpleMatch import SimpleMatch


class Test0:
    
    @staticmethod
    def test(map):
        utt = UnitTypeTable(2);
        pgs = PhysicalGameState.load(map,utt)
        gs = GameState(pgs,utt)
        ai0 = CombatRush(pgs,utt,"Light")
        ai1 = CombatRush(pgs,utt,"Heavy")
        sm = SimpleMatch()
        r = sm.playout(gs,ai0,ai1,3000,True)
        print("win = ",r)