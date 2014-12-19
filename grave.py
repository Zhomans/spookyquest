from enemy import *
from mummy import *
from eventqueue import *
from constant import *
import random
import time

#
# Grave
#
# The Enemy tries to summon a Mummy from each grave every turn
#

class Grave (Enemy):

    def __init__ (self,name):
        sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),'sprites/grave.gif')
        self._sprite = sprite

        Enemy.__init__(self,name)
        log("Grave.__init__ for "+str(self))
        self._direction = None
        self._max_actions = 0
        self._actions = self._max_actions
        
    def nearby_tiles (self):
        return self._nearby_tiles

    def move (self,dx,dy):
        pass

    def attack (self):
        pass

    def materialize (self,screen,x,y):
        #Setup nearby tiles for summoning
        EventQueue.queue.enqueue(ANIMATION_TIME,self)
        self._nearby_tiles = [(x+dx,y+dy) for (dx,dy) in DIR_TO_MOVE.values() if screen._level.tile(x+dx,y+dy) in [TYPE["Grass"],TYPE["Stone"]]]
        return Thing.materialize(self,screen,x,y)

    def summon (self):
        #Summon a Mummy
        (x,y) = random.choice(self.nearby_tiles())
        if [unit for unit in Character.units if unit.position() == (x,y)] == []:
            #A mummy won't appear if the randomly chosen place already has someone on it
            mummy = Mummy(random.choice(NAMES)).materialize(self._screen,x,y)
            mummy.add_cursor(self._cursor)
            mummy._sprite.move(TILE_SIZE*(x-self.x()),TILE_SIZE*(y-self.y())) #Place Mummy in the right spot
            mummy.set_unavailable()
            self._screen._window.update()

    def event (self,q):
        #If the Enemy is playing, summon a Mummy and end turn
        if self._alive:
            if Controllable.player == False:
                Controllable.current.switch(self)
                self.summon()
                time.sleep(GRAVE_WAIT_TIME)
                self.end_turn()
            q.enqueue(ANIMATION_TIME,self)