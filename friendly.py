from unit import *
from util import *

#
# Friendly
#
# Any unit the Player controls
# If all of them die, the Player loses
#

class Friendly (Unit):

    def __init__ (self,name):

        Unit.__init__(self,name)
        log("Friendly.__init__ for "+str(self))
        
        Character.friendlies.append(self)

        #Setup Switching
        self._next = Character.friendlies[0]
        self._previous = Character.friendlies[0] if len(Character.friendlies) < 2 else Character.friendlies[-2]
        self._next._previous = self
        self._previous._next = self

    def is_friendly (self):
        return True

    def move (self,dx,dy):
        Unit.move(self,dx,dy)

    def end_turn (self):
        #End the Turn
        self.set_unavailable()
        log("ended turn for "+str(self))
        switched = self.switch()

        #If no one to switch to, end the Player's turn
        if not switched:
            Controllable.player = False
            log("All units have ended turn. Switching to enemy turn.")
            announce(self._screen._window,"ENEMY TURN")

    def die (self,killer):
        Unit.die(self,killer)
        Character.friendlies.remove(self)

        #End the Game
        if Character.friendlies == []:
            log("All units have died. Player has lost. Game will now end.")
            lost(self._screen._window)

        #End the Turn
        if self.is_current():
            self.end_turn()