
from MicroRTS_NB.MicroRTS_NB import GameState
import time
from ai.ai import AI
from util.screen import ScreenMicroRTS

class SimpleMatch:
    
    def playout(self,gs_a :GameState,ai0 : AI,ai1:AI,max_tick : int,show_scream:True)->int:
        gs = GameState(gs_a)
        ai0.resert()
        ai1.resert()
        pgs = gs.getPhysicalGameState()
        gameover = False
    
        if show_scream :
            screen = ScreenMicroRTS(gs)
        show = True;
        
        while not gs.gameover() and gs.getTime()<3000:
            if show and show_scream   :
                    screen.draw()
                    time.sleep(0.1) 

            pa0 = ai0.getActions(gs,0)
            pa1 = ai1.getActions(gs,1)
            if show_scream:show = gs.updateScream()
              
            gs.issueSafe(pa0)
            gs.issueSafe(pa1)      
            gs.cycle()
          
             
        return gs.winner()

            
