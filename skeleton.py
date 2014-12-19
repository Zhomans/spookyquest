from friendly import *
from bonepile import *
from constant import *
from eventqueue import *

#
# Skeleton
#
# The main unit of the Player.
# If one kills another, it turns into a BonePile
#
class Skeleton (Friendly):

    DIR_TO_PIC_1 = {"Down" : 'sprites/skeleton/skeleton_down_1.gif',
                  "Up"   : 'sprites/skeleton/skeleton_up_1.gif',
                  "Right": 'sprites/skeleton/skeleton_right_1.gif',
                  "Left" : 'sprites/skeleton/skeleton_left_1.gif'}

    DIR_TO_PIC_2 = {"Down" : 'sprites/skeleton/skeleton_down_2.gif',
                  "Up"   : 'sprites/skeleton/skeleton_up_2.gif',
                  "Right": 'sprites/skeleton/skeleton_right_2.gif',
                  "Left" : 'sprites/skeleton/skeleton_left_2.gif'}

    DIR_TO_PIC_3 = {"Down" : 'sprites/skeleton/skeleton_down_3.gif',
                  "Up"   : 'sprites/skeleton/skeleton_up_3.gif',
                  "Right": 'sprites/skeleton/skeleton_right_3.gif',
                  "Left" : 'sprites/skeleton/skeleton_left_3.gif'}

    def __init__ (self,name):
        pic = Skeleton.DIR_TO_PIC_2["Down"]
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        self._sprites = Skeleton.DIR_TO_PIC_2

        Friendly.__init__(self,name)
        log("Skeleton.__init__ for "+str(self))

        #Setup for Animation
        self._frame = 0
        self._frames = [2,3,2,1]

    def is_skeleton (self):
        return True

    def die (self,killer):
        if killer.is_skeleton():
            #If it is killed by another Skeleton, it turns into a BonePile
            newTower = BonePile("Bone Pile").materialize(self._screen,self.x(),self.y())
            (dx,dy) = DIR_TO_MOVE[killer._direction]
            newTower._sprite.move(TILE_SIZE*dx,TILE_SIZE*dy)
            newTower.add_cursor(self._cursor)
        Friendly.die(self,killer)

    def materialize (self,screen,x,y):
        EventQueue.queue.enqueue(ANIMATION_TIME,self)
        return Thing.materialize(self,screen,x,y)

    def event (self,q):
        if ANIMATION:
            #Animation
            if self._alive:
                self._sprites = Skeleton.DIR_TO_PIC_2 if self._frames[self._frame] == 2 else Skeleton.DIR_TO_PIC_1 if self._frames[self._frame] == 1 else Skeleton.DIR_TO_PIC_3
                self._frame = (self._frame+1) % 4

                self._sprite.undraw()
                self._sprite = Image(self._sprite.getAnchor(),self._sprites[self._direction])
                self._sprite.draw(self._screen._window)
                self._screen.panel().redraw()
                if Controllable.current.is_cursor():            
                    self._cursor.redraw()
                self._screen._window.update()

                q.enqueue(ANIMATION_TIME,self)
      