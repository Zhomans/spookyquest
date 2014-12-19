from constant import *
from graphics import *
from controllable import *

#
# A Screen is a representation of the level displayed in the 
# viewport, with a representation for all the tiles and a 
# representation for the objects in the world currently 
# visible.
#


class Screen (object):
    def __init__ (self,level,window,cx,cy):
        self._level = level
        self._window = window
        self._cx = cx    # the initial center tile position 
        self._cy = cy    #  of the screen
        self._things = []
        self._screen = {}

        self._bg = Image(Point(WINDOW_WIDTH/2-6,WINDOW_HEIGHT/2-13),'sprites/background.gif')
        self._bg.draw(window)
            
    # return the tile at a given tile position
    def tile (self,x,y):
        return self._level.tile(x,y)

    def screen (self):
        return self._screen

    # add a thing to the screen at a given position
    def add (self,item,x,y):
        ##!! I'm not sure if this will work correctly in all cases, but as long as the cursor is defined last it should be fine.
        if Controllable.current:
            p = Controllable.current._sprite.getAnchor()
            (cx,cy) = (p.getX()-TILE_SIZE/2,p.getY()-TILE_SIZE/2)
            item.sprite().move(cx,cy)
        else:
            (cx,cy) = (self._cx,self._cy)
            item.sprite().move((x-(cx-VIEWPORT_WIDTH_RADIUS))*TILE_SIZE+SCREEN_OFFSET,
                               (y-(cy-VIEWPORT_HEIGHT_RADIUS))*TILE_SIZE+SCREEN_OFFSET)
        item.sprite().draw(self._window)
        self._things.append(item)

    def screen_pos (self,x,y):
        return (x*TILE_SIZE+SCREEN_OFFSET,y*TILE_SIZE+SCREEN_OFFSET)

    def screen_pos_index (self,index,x,y):
        x = (index % LEVEL_WIDTH) - (x - VIEWPORT_WIDTH_RADIUS)
        y = (index / LEVEL_WIDTH) - (y - VIEWPORT_HEIGHT_RADIUS)
        return self.screen_pos(x,y)

    def index (self,x,y):
        return x + (y*LEVEL_WIDTH)

    # helper method to get at underlying window
    def window (self):
        return self._window

    def add_panel (self,panel):
        self._panel = panel

    def panel (self):
        return self._panel

    #Does the actual moving of the screen
    #Probably the most important function to making everything work and look correct
    #It seems sketchy, but it does the job well
    def move(self,x,y,dx,dy):
        
        #Adjust the x-movement based on edges
        x_distance_from_edge = VIEWPORT_WIDTH_RADIUS-x if x < VIEWPORT_WIDTH_RADIUS else (x-(LEVEL_WIDTH-(VIEWPORT_WIDTH_RADIUS+1)) if x > (LEVEL_WIDTH-(VIEWPORT_WIDTH_RADIUS+1)) else 0)
        tx_distance_from_edge = VIEWPORT_WIDTH_RADIUS-x-dx if x+dx < VIEWPORT_WIDTH_RADIUS else (x+dx-(LEVEL_WIDTH-(VIEWPORT_WIDTH_RADIUS+1)) if x+dx > (LEVEL_WIDTH-(VIEWPORT_WIDTH_RADIUS+1)) else 0)
        dx = max(dx - x_distance_from_edge - tx_distance_from_edge,0) if dx > 0 else min(dx + x_distance_from_edge + tx_distance_from_edge,0)

        #Adjust the y-movement based on edges
        y_distance_from_edge = VIEWPORT_HEIGHT_RADIUS-y if y < VIEWPORT_HEIGHT_RADIUS else (y-(LEVEL_HEIGHT-(VIEWPORT_HEIGHT_RADIUS+1)) if y > (LEVEL_HEIGHT-(VIEWPORT_HEIGHT_RADIUS+1)) else 0)
        ty_distance_from_edge = VIEWPORT_HEIGHT_RADIUS-y-dy if y+dy < VIEWPORT_HEIGHT_RADIUS else (y+dy-(LEVEL_HEIGHT-(VIEWPORT_HEIGHT_RADIUS+1)) if y+dy > (LEVEL_HEIGHT-(VIEWPORT_HEIGHT_RADIUS+1)) else 0)
        dy = max(dy - y_distance_from_edge - ty_distance_from_edge,0) if dy > 0 else min(dy + y_distance_from_edge + ty_distance_from_edge,0)

        #Do the movement
        for tile in self._screen.values():
            tile.move(-dx*TILE_SIZE,-dy*TILE_SIZE)
        for thing in self._things:
            thing._sprite.move(-dx*TILE_SIZE,-dy*TILE_SIZE)
        self._bg.move(-dx*TILE_SIZE,-dy*TILE_SIZE)