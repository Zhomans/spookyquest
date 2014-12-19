import random 
from constant import *
from graphics import *
from log import *
from controllable import *
from character import *
from skeleton import *

#
# Cursor
#
# The cursor that lets the Player explore the map and select units.
# The cursor can also summon new Skeletons next to BonePiles
#

class Cursor (Controllable):
    #Singleton
    cursor = None

    def __init__ (self,name):
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2), 'sprites/cursor.gif')
        
        Controllable.__init__(self,name,"Cursor",self._sprite)
        log("Cursor.__init__ for "+str(self))
        Cursor.cursor = self

        self._direction = None

        self._max_summons = 2
        self._summons = self._max_summons

    def is_cursor (self):
        return True

    def move (self,dx,dy):
        Controllable.move(self,dx,dy)

    def switch (self,new_unit):
        return Controllable.switch(self,new_unit)

    def is_walkable (self):
        return True

    def appear(self, x, y):
        #Makes the cursor reappear at the proper location
        dx = x - self._x
        dy = y - self._y
        self.move(dx,dy)
        self._sprite.draw(self._screen.window())

    def disappear (self):
        self._sprite.undraw()

    def redraw (self):
        self._sprite.undraw()
        self._sprite.draw(self._screen._window)

    def summon (self):
        #Summoning a new skeleton
        skel = Skeleton(random.choice(NAMES)).materialize(self._screen,self.x(),self.y())
        skel.add_cursor(self)
        self.subtract_summon()
        self.update_panel()
        self._sprite.undraw()
        self._sprite.draw(self._screen._window)

    def summons (self):
        return self._summons

    def subtract_summon(self):
        self._summons -= 1

    def reset_summons(self):
        self._summons = self._max_summons

    def materialize (self,screen,x,y):
        #Allows units to have access to the cursor
        for char in Character.units:
            char.add_cursor(self)
        return Thing.materialize(self,screen,x,y)