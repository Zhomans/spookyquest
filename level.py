import random
from constant import *
#
# Hard-coded Level based off of the background image
#
class Level (object):
    def __init__ (self):
        size = LEVEL_WIDTH * LEVEL_HEIGHT
        g = TYPE["Grass"]
        s = TYPE["Stone"]
        t = TYPE["Tree"]
        v = TYPE["Grave"]
        w = TYPE["Wall"]

        level = []
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,t,t,t,t,t,t,t,t,t,g,t,t,t,t,t,t,t,t,t,t,t,t,g,g,t,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,t,t,t,t,t,t,t,t,t,g,t,t,t,t,t,t,t,t,t,t,t,g,g,g,t,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,t,t,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,t,t,t,t,t,t,t,g,g,g,t,t,t,t,t,t,t,t,t,g,g,t,t,g,g,t,t,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,t,t,t,t,t,t,t,g,g,g,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,t,g,g,t,g,g,g,g,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,t,t,t,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,t,t,t,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,t,g,g,g,g,t,t,t,t,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,g,g,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,g,g,g,t,t,t,g,g,g,g,g,g,g,g,w,w,w,w,w,w,w,w,w,w,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,g,g])
        level.extend([t,t,t,t,t,t,t,t,t,t,g,g,t,t,t,g,g,g,g,g,g,g,g,w,s,s,s,v,v,v,s,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,g,t,g,g,g])
        level.extend([t,t,t,t,t,t,t,t,t,t,g,g,g,t,g,g,g,g,g,g,g,g,g,w,s,s,s,v,v,v,v,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,g,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,v,v,v,v,v,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,g,g,t,t,t,t,g,g,g,v,v,g,v,v,g,g,g,g,g,g,g,w,s,s,s,v,v,v,v,v,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,g])
        level.extend([t,t,t,t,t,t,t,t,g,g,g,v,v,g,v,v,g,g,v,v,g,g,g,w,s,s,s,v,v,v,v,v,s,w,g,g,v,v,v,g,g,g,g,g,v,v,v,g,g,g,g,g,g,g,g,t,t])
        level.extend([t,t,t,t,g,t,t,t,g,g,g,g,g,g,g,g,g,g,v,v,g,g,g,w,s,s,s,v,v,v,v,v,s,w,g,g,v,v,v,g,g,v,v,g,v,v,v,g,g,g,g,g,g,g,t,t,t])
        level.extend([t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,v,v,v,v,v,s,w,g,g,v,v,v,g,g,g,g,g,g,g,g,g,g,v,v,g,g,g,g,t,t])
        level.extend([g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,s,s,s,v,v,s,w,g,g,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,v,v,g,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,g,g,g,g,g,g,g,v,v,v,g,v,v,v,g,g,g,w,w,w,w,w,s,s,s,w,w,w,w,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,g,g,g,g,g,g,g,v,v,v,g,v,v,v,g,g,g,w,w,w,w,w,s,s,s,w,w,w,w,w,g,v,v,v,g,g,v,v,v,g,v,v,v,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,v,v,v,g,g,g,w,w,w,s,s,s,s,s,s,s,w,w,w,g,v,v,v,g,g,v,v,v,g,v,v,v,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,v,v,v,g,g,g,g,w,v,v,v,s,s,s,v,v,v,w,g,g,v,v,v,g,g,v,v,v,g,v,v,v,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,v,v,v,g,g,g,g,w,v,v,v,s,s,s,v,v,v,w,g,g,v,v,v,g,g,v,v,v,g,v,v,v,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,v,v,v,s,s,s,v,v,v,w,g,g,v,v,v,g,g,v,v,v,g,v,v,v,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,v,v,v,s,s,s,v,v,v,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,t,g,g,g,g,v,v,g,g,g,g,g,g,g,g,g,g,g,w,v,v,v,s,s,s,v,v,v,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,t,g,v,v,g,g,g,g,g,v,v,v,v,v,v,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,t,g,v,v,g,g,g,g,g,v,v,v,v,v,v,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,t,g,g,v,v,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,s,s,s,s,s,s,s,s,s,w,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,w,w,s,s,s,s,s,s,s,w,w,w,g,g,g,g,v,v,g,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,w,w,w,w,w,s,s,s,w,w,w,w,w,g,g,g,g,v,v,g,v,v,v,g,v,v,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,g,g,g,g,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g,w,w,w,g,g,s,s,s,g,g,w,w,w,g,g,g,g,g,g,g,g,g,g,g,v,v,g,g,g,g,g,g,g,g,g])
        level.extend([t,t,t,t,g,g,g,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t])
        level.extend([t,t,t,t,t,g,g,v,v,v,g,g,v,v,g,v,v,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,v,v,v,g,g,g,g,g,v,v,g,g,g,g,g,g,v,v,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g,g,v,v,v,g,s,s,s,g,g,g,g,g,v,v,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,v,v,v,g,g,g,g,g,g,g,g,g,g,g,g,g,v,v,v,g,s,s,s,g,g,g,v,v,v,v,g,g,v,v,v,g,g,g,v,v,v,g,g,g,g,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,v,v,v,g,s,s,s,g,g,v,v,v,v,g,g,g,v,v,v,g,g,g,v,v,v,g,g,g,g,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,v,v,v,g,s,s,s,g,v,v,v,v,g,g,g,g,v,v,v,g,g,g,v,v,v,g,g,t,g,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,v,v,v,g,s,s,s,g,v,v,v,g,g,g,g,g,v,v,v,g,g,g,v,v,v,g,t,t,g,g,g,g,t,t])
        level.extend([t,t,t,t,t,t,t,t,g,g,g,v,v,g,g,v,g,g,g,g,g,g,g,v,v,g,g,s,s,s,g,g,g,v,g,g,g,g,g,v,v,v,g,g,g,v,v,v,g,t,t,t,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,v,g,g,g,g,g,v,v,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,v,v,v,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,v,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,v,v,v,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,v,v,v,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,g,g,g,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,g,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,t,t,t])
        level.extend([t,t,t,t,g,g,t,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,g,g,t,t,t])
        level.extend([t,t,t,g,g,g,t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,t,t,t,g,g,g,t])
        level.extend([t,t,t,t,g,g,g,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t,g,t,t,t])
        level.extend([t,t,t,t,g,g,g,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t])
        level.extend([t,t,t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t])
        level.extend([t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,t,t,t])
        level.extend([t,t,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])
        level.extend([g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,s,s,s,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g])

        self._map = level

    def _pos (self,x,y):
        return x + (y*LEVEL_WIDTH);

    # return the tile at a given tile position in the level
    def tile (self,x,y):
        return self._map[self._pos(x,y)]

    def map (self):
        return self._map