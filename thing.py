from root import *
from constant import *
from graphics import *
from log import *
# A thing is something that can be interacted with and by default
# is not moveable or walkable over
#
#   Thing(name,description)
#
# 
class Thing (Root):
    def __init__ (self,name,desc):
        self._name = name
        self._description = desc
        self._sprite = Text(Point(TILE_SIZE/2,TILE_SIZE/2),"?")
        log("Thing.__init__ for "+str(self))

    def __str__ (self):
        return "<"+self.name()+">"

    # return the sprite for display purposes
    def sprite (self):
        return self._sprite

    # return the name
    def name (self):
        return self._name

    # return the position of the thing in the level array
    def position (self):
        return (self._x,self._y)
        
    def x (self):
        return self._x

    def y (self):
        return self._y
        
    # return the description
    def description (self):
        return self._description

    # creating a thing does not put it in play -- you have to 
    # call materialize, passing in the screen and the position
    # where you want it to appear
    def materialize (self,screen,x,y):
        screen.add(self,x,y)
        self._screen = screen
        self._x = x
        self._y = y
        return self

    def is_thing (self):
        return True

    def is_walkable (self):
        return False
