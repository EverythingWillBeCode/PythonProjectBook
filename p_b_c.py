from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.uix.foatlayout import Floatlayout

__version__ = "0.1"

class BreakoutApp(App):
    pass

BreakoutApp().run()

from kivy.properties import (ListProperty, NumericProperty, ObjectProperty, StringProperty)
class Game(Floatlayout):
        blocks = ListProperty([])
        player = ObjectProperty()
        ball = ObjectProperty()

class player(Widget):
        position = NumericProperty(0.5)
        direction = StringProperty("none")

class Ball(Widget):
        pos_hint_x = NumericProperty(0.5)
        pos_hint_y = NumericProperty(0.3)
        proper_size = NumericProperty(0.)
        velocity = ListProperty([0.1, 0.5])

class Block(Widget):
        colour = ListProperty([1, 0, 0])

from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

class Player(Widget):
    def __init__(self, **kwargs):
           super(Player, self).__init__(**kwargs)
           with self.canvas:
                  Color(1, 0, 0, 1)
                  Rectangle(pos=self.pos, size=self.size)

import random

class Block(Widget):
    def __init__(self, **kwargs):
          super(Block, self).__init__(**kwargs)
          self.colour = random.choice([(0.78, 0.28, 0), (0.28, 0.63, 0.28), (0.25, 00.28, 0.78)])

<Block>
