import ability
import time
import pyglet
from pyglet import clock
from pyglet.window import key


class Charactor(pyglet.sprite.Sprite):
    def __init__(self, name, hp=100, *args, **kwargs):
        super(Charactor, self).__init__(*args, **kwargs)
        self.name = name
        self.hp = hp
        self.dead = False
        self.status = []
        self.abilities = []

        self.clock = time.time()
        self.event_handlers = []

    def update(self, dt):
        for status in self.status:
            status.effect()
        if self.hp <= 0 and not self.dead:
            self.dead = True
            print self.name, 'is dead.'

class Player(Charactor):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)


        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            ability.basic_attack.cast(self, self.target)


class NPC(Charactor):

    def update(self, dt):
        super(NPC, self).update(dt)
        if time.time() - self.clock > 1.0 and not self.dead and not self.target.dead:
            ability.basic_attack.cast(self, self.target)
            self.clock = time.time()



