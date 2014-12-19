from constant import *
from graphics import *
#
# Create the right-side panel that can be used to display interesting
# information to the Unit
#

class Panel(object):
    def __init__(self,window):
        self._window = window

        background = Rectangle(Point(WINDOW_WIDTH+1,-20),
                       Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL+20,WINDOW_HEIGHT+20))
        background.setFill("darkgray")
        background.setOutline("darkgray")
        background.draw(window)
        self._background = background

        self._border = Image(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2+SCREEN_OFFSET, WINDOW_HEIGHT/2+2*SCREEN_OFFSET),'sprites/gothic.gif')
        self._border.draw(window)

        title_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,
                        60),"Spooky Quest")
        title_text.setSize(28)
        title_text.setStyle("bold")
        title_text.setFill("steelblue")
        title_text.setFace("courier")
        title_text.draw(window)
        self._title_text = title_text

        title_divider = Line(Point(WINDOW_WIDTH+25,90),Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL-25,90))
        title_divider.setWidth(3)
        title_divider.draw(window)
        self._title_divider = title_divider

        tile_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,140),"Shouldn't Be Visible")
        tile_text.setSize(20)
        tile_text.setStyle("bold")
        tile_text.setFill("black")
        tile_text.setFace("courier")
        tile_text.draw(window)
        self._tile_text = tile_text

        unit_divider = Line(Point(WINDOW_WIDTH+50,190),Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL-50,190))
        unit_divider.setWidth(3)
        unit_divider.draw(window)
        self._unit_divider = unit_divider

        unit_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,220),"")
        unit_text.setSize(24)
        unit_text.setStyle("bold")
        unit_text.setFill("black")
        unit_text.setFace("courier")
        unit_text.draw(window)
        self._unit_text = unit_text

        health_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,260),"")
        health_text.setSize(24)
        health_text.setStyle("bold")
        health_text.setFill("black")
        health_text.setFace("courier")
        health_text.draw(window)
        self._health_text = health_text

        facing_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,325),"")
        facing_text.setSize(24)
        facing_text.setStyle("bold")
        facing_text.setFill("black")
        facing_text.setFace("courier")
        facing_text.draw(window)
        self._facing_text = facing_text

        facing_health_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,375),"")
        facing_health_text.setSize(24)
        facing_health_text.setStyle("bold")
        facing_health_text.setFill("black")
        facing_health_text.setFace("courier")
        facing_health_text.draw(window)
        self._facing_health_text = facing_health_text

        actions_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,490),"")
        actions_text.setSize(24)
        actions_text.setStyle("bold")
        actions_text.setFill("black")
        actions_text.setFace("courier")
        actions_text.draw(window)
        self._actions_text = actions_text

        actions_summons_divider = Line(Point(WINDOW_WIDTH+50,530),Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL-50,530))
        actions_summons_divider.setWidth(3)
        actions_summons_divider.draw(window)
        self._actions_summons_divider = actions_summons_divider

        summons_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,575),"")
        summons_text.setSize(24)
        summons_text.setStyle("bold")
        summons_text.setFill("black")
        summons_text.setFace("courier")
        summons_text.draw(window)
        self._summons_text = summons_text

        controls_divider = Line(Point(WINDOW_WIDTH+25,620),Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL-25,620))
        controls_divider.setWidth(3)
        controls_divider.draw(window)
        self._controls_divider = controls_divider

        controls_text = Text(Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL/2,650),"q/w: Switch Unit  e: End turn\na: De-select  s: Summon  d: Select")
        controls_text.setSize(10)
        controls_text.setStyle("bold")
        controls_text.setFill("black")
        controls_text.setFace("courier")
        controls_text.draw(window)
        self._controls_text = controls_text

    def background (self):
        return self._background

    def title_text (self):
        return self._title_text

    def tile_text (self):
        return self._tile_text

    def set_tile_text (self,text):
        self._tile_text.setText(text)

    def unit_text (self):
        return self._unit_text

    def set_unit_text (self,text):
        self._unit_text.setText(text)

    def health_text (self):
        return self._health_text

    def set_health_text (self,text):
        self._health_text.setText(text)

    def facing_text (self):
        return self._facing_text

    def set_facing_text (self,text):
        self._facing_text.setText(text)

    def facing_health_text (self):
        return self._facing_health_text

    def set_facing_health_text (self,text):
        self._facing_health_text.setText(text)

    def actions_text (self):
        return self._actions_text

    def set_actions_text (self,text):
        self._actions_text.setText(text)

    def summons_text (self):
        return self._summons_text

    def set_summons_text (self,text):
        self._summons_text.setText(text)

    def controls_text (self):
        return self._controls_text

    def set_controls_text (self,text):
        self._controls_text.setText(text)

    def redraw (self):
        self._background.undraw()
        self._background.draw(self._window)
        self._border.undraw()
        self._border.draw(self._window)
        self._title_text.undraw()
        self._title_text.draw(self._window)
        self._title_divider.undraw()
        self._title_divider.draw(self._window)
        self._tile_text.undraw()
        self._tile_text.draw(self._window)
        self._unit_text.undraw()
        self._unit_text.draw(self._window)
        self._health_text.undraw()
        self._health_text.draw(self._window)
        self._facing_text.undraw()
        self._facing_text.draw(self._window)
        self._facing_health_text.undraw()
        self._facing_health_text.draw(self._window)
        self._actions_text.undraw()
        self._actions_text.draw(self._window)
        self._actions_summons_divider.undraw()
        self._actions_summons_divider.draw(self._window)
        self._unit_divider.undraw()
        self._unit_divider.draw(self._window)
        self._summons_text.undraw()
        self._summons_text.draw(self._window)
        self._controls_divider.undraw()
        self._controls_divider.draw(self._window)
        self._controls_text.undraw()
        self._controls_text.draw(self._window)