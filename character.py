from thing import *
from constant import *
from log import *
import graphics
#
# Character 
# Anything that can move is a character
#
class Character (Thing):
    units = []
    friendlies = []
    enemies = []

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))

        #Default image for characters
        rect = Rectangle(Point(0,0),
                         Point(TILE_SIZE,TILE_SIZE))
        rect.setFill("red")
        rect.setOutline("red")
        self._sprite = rect
        
        self._direction = "Down"
        self._health = CHARACTER_HEALTH


    def health (self):
        return self._health

    def reduce_health (self,damage,attacker):
        self._health -= damage
        if self._health <= 0:
            self.die(attacker)

    def move (self,dx,dy):
        #Moves the screen and characters appropriately

        if self.is_unit():
            #Switch Directions when moving
            self.switch_direction(MOVE_TO_DIR[(dx,dy)])

        tx = self._x + dx
        ty = self._y + dy

        if tx >= 0 and ty >= 0 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if self.is_cursor():
                #If cursor, don't worry about movement limits
                self.move_screen_and_character(dx,dy)

                self._x = tx
                self._y = ty
                return True
            else:
                if self._screen._level.tile(tx,ty) in [TYPE["Grass"],TYPE["Stone"]]:
                    #Can only walk on Grass or Stone
                    if not [thing for thing in self._screen._things if thing.position() == (tx,ty) and not thing.is_walkable()]:
                        #If nothing else is already there, move
                        self.move_screen_and_character(dx,dy)

                        self._x = tx
                        self._y = ty
                        return True
        return False

    def is_character (self):
        return True

    def is_walkable (self):
        return False

    def move_screen_and_character(self,dx,dy):
        #Moves the screen and characters
        division = 1 if self.is_cursor() else MOVEMENT_DIVISIONS

        for i in range(int(division)):
            #Separates movement into chunks to make it appear more fluid
            if self.is_current():
                self._screen.move(self._x,self._y,dx/division,dy/division)
            self._sprite.move(dx*TILE_SIZE/division,dy*TILE_SIZE/division)
            self._screen._window.update()
            self._x += dx/division
            self._y += dy/division

    def switch_direction (self,direction):
        self._direction = direction

    def attack (self):
        #Attack in the direction the character is currently facing
        (dx,dy) = DIR_TO_MOVE[self._direction]
        tx = self._x + dx
        ty = self._y + dy
        try: 
            #Stop at the first thing that is in front of you. This should save time.
            target = next(unit for unit in Character.units if unit.position() == (tx,ty))
            log(self.name() + " attacked " + target.name() + " for 1 damage")

            #Nice movement animation when attacking
            self.move_screen_and_character(dx*.5,dy*.5)
            self.move_screen_and_character(-dx*.5,-dy*.5)
            (self._x,self._y) = (int(self.x()),int(self.y())) #Need this because moving in non-int increments makes them floats

            target.reduce_health(1,self)
            self.subtract_action()
            self.update_panel() ##!! This will cause problems if a non-controllable tries to attack, but in the current code there is no non-controllable characters
            
            if self._actions == 0 and self.is_friendly():
                #Enemies end turn on their own
                self.end_turn()

            return target
        except StopIteration:
            pass

    def subtract_action (self):
        pass