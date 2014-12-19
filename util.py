#Other functions that didn't really fit anywhere in particular

from constant import *
from graphics import *

def lost (window):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),'YOU LOST!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)

def win (window):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),'YOU WIN!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)

def announce (window,text):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),text)
    t.setSize(36)
    t.setTextColor('blue')
    t.draw(window)
    window.getKey()
    t.undraw()
