import time
from character import *
from constant import *
from log import *

#
# Controllable
#
# Anything that can be controlled, either by the Player or the Enemy, is controlable
#
class Controllable (Character):
    current = None # The controllable that is currently being controlled. Very important!
    player = True # True is the Player is in control. False if the Enemy is in control.

    def __init__ (self,name,desc,sprite):
        Character.__init__(self,name,desc)
        log("Controllable.__init__ for "+str(self))
        self._sprite = sprite
        
    def is_current (self):
        return Controllable.current == self

    def set_as_current (self):
        #Set this object as the current object. 
        #This also involved moving the screen to be on this object.
        if not Controllable.current:
            old_x = self._screen._cx
            old_y = self._screen._cy
            division = 1
        else:
            old_x = Controllable.current.x()
            old_y = Controllable.current.y() 
            division = SWITCH_DIVISIONS

        dx = self.x()-old_x
        dy = self.y()-old_y

        for i in range(int(division)):
            self._screen.move(old_x,old_y,dx/division,dy/division)
            self._screen._window.update()
            old_x += dx/division
            old_y += dy/division

        Controllable.current = self        
        self.update_panel()
        self._screen._window.update()


    def is_controllable (self):
        return True

    def end_turn (self):
        pass

    def move (self,dx,dy):
        moved = Character.move(self,dx,dy)
        self.update_panel()
        return moved

    def switch (self,new_unit):
        new_unit.set_as_current()
        log("switched unit to " + str(new_unit))
        return True

    def update_panel (self):
        #Update the side panel with all of the new information regarding the current object.
        self.update_panel_tile_text()
        self.update_panel_unit_text()
        self.update_panel_facing_text()
        self.update_panel_summons_text()
        self.update_panel_controls_text()
        self._screen.panel().redraw()


    #Helper functions to update the panel
    #A lot of manual text here
    def update_panel_tile_text (self):
        if Controllable.current.is_cursor():
            tile_type = NUM_TO_TYPE[self._screen.tile(Controllable.current.x(),Controllable.current.y())]
            can_walk = "Traversable" if tile_type in ["Stone","Grass"] else "Impassable"
            self._screen.panel().set_tile_text(tile_type+"\n"+can_walk)
        else:
            self._screen.panel().set_tile_text("")

    def update_panel_unit_text (self):
        try: 
            unit = next(unit for unit in Character.units if unit.position() == Controllable.current.position())
            self._screen.panel().set_unit_text(unit.name())
            self._screen.panel().set_health_text(str(unit.health())+" Health")
            self._screen.panel().set_actions_text("Actions\n" + str(unit.actions()))

        except StopIteration:
            self._screen.panel().set_unit_text("")
            self._screen.panel().set_health_text("")
            self._screen.panel().set_actions_text("")

    def update_panel_facing_text (self):
        try: 
            (dx,dy) = DIR_TO_MOVE[self._direction]
            facing = next(unit for unit in Character.units if unit.position() == (Controllable.current.x()+dx,Controllable.current.y()+dy))
            self._screen.panel().set_facing_text("---vs---\n" + facing.name())
            self._screen.panel().set_facing_health_text(str(facing.health())+" Health")
        except (StopIteration, KeyError):
            self._screen.panel().set_facing_text("")
            self._screen.panel().set_facing_health_text("")

    def update_panel_summons_text (self):
        if Controllable.current and Controllable.current.is_cursor():
            self._screen.panel().set_summons_text("Summons\n" + str(Controllable.current.summons()))
        else:
            self._screen.panel().set_summons_text("")

    def update_panel_controls_text (self):
        if Controllable.current.is_cursor():
            self._screen.panel().set_controls_text("q/w: None  e: None\na: None  s: Summon  d: Select")
        elif Controllable.current.is_friendly():
            self._screen.panel().set_controls_text("q/w: Switch Unit  e: End turn\na: De-select  s: None  d: Attack")
        else:
            self._screen.panel().set_controls_text("")
