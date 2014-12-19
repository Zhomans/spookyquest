from friendly import *

#
# BonePile
#
# Player can summon new Skeletons next to BonePiles
#

class BonePile (Friendly):

    def __init__ (self,name):
        sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),'sprites/bone_pile.gif')
        self._sprite = sprite

        Friendly.__init__(self,name)
        log("BonePile.__init__ for "+str(self))
        self._direction = None
        self.set_unavailable() # Can't be targetted
        self._max_actions = 0 # Can't perform actions
        self._actions = self._max_actions

        
    def nearby_tiles (self):
        return self._nearby_tiles

    def move (self,dx,dy):
        pass

    def set_available (self):
        pass

    def end_turn (self):
        pass

    def attack (self):
        pass

    def is_bone_pile (self):
        return True

    def materialize (self,screen,x,y):
        #Setup tiles where units can be summoned
        self._nearby_tiles = [(x+dx,y+dy) for (dx,dy) in DIR_TO_MOVE.values()]
        return Thing.materialize(self,screen,x,y)