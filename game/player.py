import pyglet
import charactor
from pyglet.window import key

class Player(charactor.Charactor):
    '''Grants keyboard input to controlled Charactor.'''
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.facing_x = 'East'
        self.facing_y = 'Neutral'

    def on_key_press(self, symbol, modifiers):
        '''Currently mapped to a list of abilities. Hopefully
        this makes it easier to switch abilities later.'''
        if symbol == key._1:
            self.abilities[1].cast(self, self.target)
        elif symbol == key._2:
            self.abilities[2].cast(self, self.target)
        elif symbol == key._3:
            self.abilities[3].cast(self, self.target)
        elif symbol == key._4:
            self.abilities[4].cast(self, self.target)
    
    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def update(self, dt):
        super(Player, self).update(dt)
        self.dx = 0
        self.dy = 0
        if self.key_handler[key.W]:
            self.dy = 2.5
            self.facing_y = 'North'
        elif self.key_handler[key.S]:
            self.dy = -2.5
            self.facing_y = 'South'
        else:
            self.facing_y = 'Neutral'

        if self.key_handler[key.A]:
            self.dx = -2.5
            self.facing_x = 'West'
        elif self.key_handler[key.D]:
            self.dx = 2.5
            self.facing_x = 'East'
        else:
            self.facing_x = 'Neutral'

        #print self.facing_x + self.facing_y
        # NOTE: direction facing is always going to be updating
        # so when animating, NEUTRAL signifies to KEEP AS BEFORE!!!
