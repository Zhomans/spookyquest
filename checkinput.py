from constant import *
from controllable import *
from log import *
from character import *
from cursor import *

# A simple event class that checks for user input.
# It re-enqueues itself after the check.

class CheckInput (object):
    def __init__ (self,window,unit):
        log("starting out as "+str(unit))
        self._window = window

    def event (self,q):
        if Controllable.player:
            key = self._window.checkKey()

            #Escape
            if key == 'Escape':
                self._window.close()
                exit(0)

            #Movement
            elif key in DIR_TO_MOVE:
                if Controllable.current.is_cursor() or Controllable.current.is_friendly():
                    (dx,dy) = DIR_TO_MOVE[key]
                    Controllable.current.move(dx,dy)

            #Switch Forward
            elif key == 'w':
                if Controllable.current.is_unit():
                    Controllable.current.switch()

            #Switch Backwards
            elif key == 'q':
                if Controllable.current.is_unit():
                    Controllable.current.switch(None,"Previous")

            #End Turn Manually
            elif key == 'e':
                if Controllable.current.is_unit():
                    Controllable.current.end_turn()

            #Select/Attack
            elif key == 'd':
                if Controllable.current.is_cursor():
                    try:
                        cursor = Controllable.current
                        selected = next(unit for unit in Character.units if unit.position() == cursor.position() and unit.is_available())
                        cursor.disappear()
                        cursor.switch(selected)
                    except StopIteration:
                        pass
                elif Controllable.current.is_friendly():
                    Controllable.current.attack()

            #De-select
            elif key == 'a':
                if Controllable.current.is_unit():
                    unit = Controllable.current
                    Cursor.cursor.appear(unit.x(),unit.y())
                    Controllable.current.switch(Cursor.cursor)

            #Summon
            elif key == 's':
                if Controllable.current.is_cursor():
                    if Controllable.current.summons() > 0:
                        if [unit for unit in Character.units if unit.position() == Controllable.current.position()] == []:
                            tile_type = Controllable.current._screen._level.tile(Controllable.current.x(),Controllable.current.y())
                            if tile_type in [TYPE["Grass"],TYPE["Stone"]]:
                                if Controllable.current.position() in [tile for tower_tiles in [tower.nearby_tiles() for tower in Character.friendlies if tower.is_bone_pile()] for tile in tower_tiles]:
                                    Controllable.current.summon()

        q.enqueue(1,self)