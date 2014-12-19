from unit import *
from controllable import *
from constant import *
from cursor import *

#
# Enemy
#
# Any unit controlled by the enemy
# All must be killed to win
#

class Enemy (Unit):

    def __init__ (self,name):

        Unit.__init__(self,name)
        log("Enemy.__init__ for "+str(self))
        
        Character.enemies.append(self)

        #Setup Switching
        self._next = Character.enemies[0]
        self._previous = Character.enemies[0] if len(Character.enemies) < 2 else Character.enemies[-2]
        self._next._previous = self
        self._previous._next = self

    def is_enemy (self):
        return True

    def move (self,dx,dy):
        return Unit.move(self,dx,dy)

    def end_turn (self):
        #Ending Turn
        self.set_unavailable()
        log("ended turn for "+str(self))
        
        #If no units can move, end the Enemy's turn
        remaining = [enemy for enemy in Character.enemies if enemy.is_available()]
        if remaining == []:
            Controllable.player = True
            log("All enemies have ended turn. Switching to player turn.")
            for friendly in Character.friendlies:
                friendly.set_available()
            unit = Character.friendlies[0]
            Controllable.current.switch(unit)
            Cursor.cursor.appear(unit.x(),unit.y())
            Cursor.cursor.reset_summons()
            Controllable.current.switch(Cursor.cursor)
            announce(self._screen._window,"PLAYER TURN")

            for enemy in Character.enemies:
                #This is necessary so that the Player can select the enemies on the Player's turn
                enemy.set_available()

    def die (self,killer):
        Unit.die(self,killer)
        Character.enemies.remove(self)

        #End The Game
        if Character.enemies == []:
            self.update_panel()
            log("All enemies have died. Player has won. Game will now end.")
            win(self._screen._window)

        #End The Turn
        if self.is_current():
            self.end_turn()
