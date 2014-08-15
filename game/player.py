import pyglet
import charactor
from pyglet.window import key

class Player(charactor.Charactor):
    '''Grants keyboard input to controlled Charactor.'''
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def on_key_press(self, symbol, modifiers):
        if symbol == key._1:
            self.abilities[1].cast(self, self.target)
        elif symbol == key._2:
            self.abilities[2].cast(self, self.target)
        elif symbol == key._3:
            self.abilities[3].cast(self, self.target)
        elif symbol == key._4:
            self.abilities[4].cast(self, self.target)

    def update(self, dt):
        super(Player, self).update(dt)
        self.dx = 0
        self.dy = 0
        if self.key_handler[key.W]:
            self.dy = 2.5
        if self.key_handler[key.S]:
            self.dy = -2.5
        if self.key_handler[key.A]:
            self.dx = -2.5
        if self.key_handler[key.D]:
            self.dx = 2.5
