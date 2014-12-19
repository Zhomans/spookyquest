from enemy import *
from constant import *
from log import *
from eventqueue import *
from friendly import *
#
# Mummy
#
# The main type of Enemy
#
class Mummy (Enemy):

    DIR_TO_PIC_1 = {"Down" : 'sprites/mummy/mummy_down_1.gif',
                  "Up"   : 'sprites/mummy/mummy_up_1.gif',
                  "Right": 'sprites/mummy/mummy_right_1.gif',
                  "Left" : 'sprites/mummy/mummy_left_1.gif'}

    DIR_TO_PIC_2 = {"Down" : 'sprites/mummy/mummy_down_2.gif',
                  "Up"   : 'sprites/mummy/mummy_up_2.gif',
                  "Right": 'sprites/mummy/mummy_right_2.gif',
                  "Left" : 'sprites/mummy/mummy_left_2.gif'}

    DIR_TO_PIC_3 = {"Down" : 'sprites/mummy/mummy_down_3.gif',
                  "Up"   : 'sprites/mummy/mummy_up_3.gif',
                  "Right": 'sprites/mummy/mummy_right_3.gif',
                  "Left" : 'sprites/mummy/mummy_left_3.gif'}

    def __init__ (self,name):
        pic = Mummy.DIR_TO_PIC_2["Down"]
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        self._sprites = Mummy.DIR_TO_PIC_2

        Enemy.__init__(self,name)
        log("Mummy.__init__ for "+str(self))

        #Setup Animation
        self._frame = 0
        self._frames = [2,3,2,1]


    def materialize (self,screen,x,y):
        EventQueue.queue.enqueue(ANIMATION_TIME,self)
        return Thing.materialize(self,screen,x,y)

    def event (self,q):
        if self._alive:
            if ANIMATION:
                #Animation
                self._sprites = Mummy.DIR_TO_PIC_2 if self._frames[self._frame] == 2 else Mummy.DIR_TO_PIC_1 if self._frames[self._frame] == 1 else Mummy.DIR_TO_PIC_3
                self._frame = (self._frame+1) % 4
                
                self._sprite.undraw()
                self._sprite = Image(self._sprite.getAnchor(),self._sprites[self._direction])
                self._sprite.draw(self._screen._window)
                self._screen.panel().redraw()
                if Controllable.current.is_cursor():            
                    self._cursor.redraw()
                self._screen._window.update()

            if Controllable.player == False:
                #Move and Attack if it's the Enemy's turn
                Controllable.current.switch(self)
                while self._actions > 0:
                    self.move_and_attack()
                    time.sleep(.1)
                self.end_turn()

            q.enqueue(ANIMATION_TIME,self)


    def move_and_attack (self):
        ## Completely Random
        # (dx,dy) = random.choice(DIR_TO_MOVE.values())
        # Enemy.move(self,dx,dy)


        #Probably the worst AI ever created, but it's good enough for the purposes of this game
        #Often gets stuck or does stupid things
        #But it's not very intensive
        #Could easily be cleaned up to be more efficent

        nearest_friendly = None
        friendly_distance = LEVEL_WIDTH*LEVEL_HEIGHT

        for friendly in Character.friendlies:
            (fx,fy) = friendly.position()
            distance = abs(fx-self.x())+abs(fy-self.y())
            if distance < friendly_distance:
                nearest_friendly = (fx,fy)
                friendly_distance = distance
                if distance == 1:
                    break

        (dx,dy) = (nearest_friendly[0]-self.x(),nearest_friendly[1]-self.y())
        choices = []
        if dx > 0:
            choices.append((1,0))
        elif dx < 0:
            choices.append((-1,0))

        if dy > 0:
            choices.append((0,1))
        elif dy < 0:
            choices.append((0,-1))

        (dx,dy) = random.choice(choices)
        choices.remove((dx,dy))
        moved = Enemy.move(self,dx,dy)

        if friendly_distance != 1:
            while not moved:
                if choices != []:
                    (dx,dy) = random.choice(choices)
                    choices.remove((dx,dy))
                else:
                    (dx,dy) = random.choice(DIR_TO_MOVE.values())
                moved = Enemy.move(self,dx,dy)
        else:
            if self._actions > 0:
                self.attack()



            