############################################################
#
# Spooky Quest
#
# A Game Programming Final Project
#
# Zach Homans
#
# Fall 2014
#

import time
import random
from constant import *
from level import *
from screen import *
from log import *
from eventqueue import *
from checkinput import *
from cursor import *
from panel import *
from skeleton import *
from bonepile import *
from grave import *
from mummy import *

#
# The main() function
# 
# It initializes everything that needs to be initialized.
# Order is important for graphics to display correctly.
# More specifically, the cursor must be materialized last.
# Note that autoflush=False, so we need to explicitly
# call window.update() to refresh the window when we make
# changes
#

def main ():
    #Setup the window
    window = GraphWin("Spooky Quest", 
                      WINDOW_WIDTH+WINDOW_RIGHTPANEL, WINDOW_HEIGHT,
                      autoflush=False)

    #Setup the level
    level = Level()
    log ("level created")

    #Setup the screen and panel
    scr = Screen(level,window,LEVEL_WIDTH/2,LEVEL_HEIGHT/2)
    log ("screen created")
    panel = Panel(window)
    scr.add_panel(panel)
    log ("panel created")

    #Initiatize the Event Queue
    q = EventQueue()

    #Spawn the Player's characters
    Skeleton(random.choice(NAMES)).materialize(scr,28,70)
    Skeleton(random.choice(NAMES)).materialize(scr,30,70)
    Skeleton(random.choice(NAMES)).materialize(scr,26,70)
    Skeleton(random.choice(NAMES)).materialize(scr,28,72)

    BonePile("Bone Pile").materialize(scr,27,71)
    BonePile("Bone Pile").materialize(scr,29,71)

    #Spawn the Enemy's Graves
    grave_count = GRAVE_COUNT
    graves = []
    while grave_count > 0:
        #Prevents graves from starting close to the player
        (x,y) = (random.randint(1,LEVEL_WIDTH),random.randint(1,LEVEL_HEIGHT-10)) #Arbitrary Limits
        tile_type = scr._level.tile(x,y)
        if (x,y) not in graves and tile_type in [TYPE["Grass"],TYPE["Stone"]]:
            Grave("Tombstone").materialize(scr,x,y)
            graves.append((x,y))
            grave_count -= 1

    #Spawn Cursor
    c = Cursor("Cursor").materialize(scr,28,72).set_as_current()
    
    #Setup input checking
    q.enqueue(1,CheckInput(window,c))

    #Main Loop
    while True:
        # Grab the next event from the queue if it's ready
        q.dequeue_if_ready()
        # Time unit = 10 milliseconds
        time.sleep(QUEUE_TIMESTEP)

if __name__ == '__main__':
    main()
