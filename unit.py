from constant import *
from graphics import *
from log import *
from controllable import *
from util import *

#
# Unit
#
# Controllables that have limited action
# Friendlies and Enemies include
#
class Unit (Controllable):

    def __init__ (self,name):        
        Controllable.__init__(self,name,"Unit",self._sprite)
        log("Unit.__init__ for "+str(self))
        self._available = True
        self._max_actions = MAX_ACTIONS
        self._actions = self._max_actions

        Character.units.append(self)
        self._alive = True

    def is_available (self):
        return self._available

    def set_unavailable (self):
        self._available = False

    def set_available (self):
        self._available = True
        self._actions = self._max_actions

    def actions (self):
        return self._actions

    def is_unit (self):
        return True

    def move (self,dx,dy):
        if self._actions > 0:
            self.subtract_action()
            if not Controllable.move(self,dx,dy):
                # A dirty way to reverse using an action if it doesn't end up moving
                # Required so that the panel updated correctly
                self.add_action()
                self.update_panel() 
                return False
            if self._actions == 0 and self.is_friendly():
                #Enemies end turn on their own
                self.end_turn()
            return True

    def subtract_action(self):
        self._actions -= 1

    def add_action (self):
        self._actions += 1

    def switch (self,new_unit=None,direction="Next"):
        #Switching
        #Has directionality if no unit is selected
        if not new_unit:
            ##!! There's totally a better way of doing this
            if direction == "Next":
                new_unit = self._next
                while not new_unit.is_available():
                    new_unit = new_unit._next
                    if new_unit == self:
                        return False
            elif direction == "Previous":
                new_unit = self._previous
                while not new_unit.is_available():
                    new_unit = new_unit._previous
                    if new_unit == self:
                        return False
            else:
                log("Invalid direction used.")
        
        return Controllable.switch(self,new_unit)

    def switch_direction (self,direction):
        #Switches direction and changes the sprite appropriately

        Character.switch_direction(self,direction)
        self._sprite.undraw()
        self._sprite = Image(self._sprite.getAnchor(),self._sprites[direction])
        self._sprite.draw(self._screen._window)
        self._screen.panel().redraw()

        self._screen._window.update()

    def die (self,killer):
        self._next._previous = self._previous
        self._previous._next = self._next
        self._sprite.undraw()
        Character.units.remove(self)
        log(str(self)+" has died")
        self._alive = False

    def is_walkable (self):
        return not self._alive

    def add_cursor (self,cursor):
        self._cursor = cursor